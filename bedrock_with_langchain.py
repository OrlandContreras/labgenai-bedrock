import boto3
import botocore
import json
from langchain.llms.bedrock import Bedrock
from langchain.prompts import PromptTemplate


boto3_bedrock = boto3.client("bedrock-runtime")

inference_modifier = {
    "max_tokens_to_sample": 4096,
    "temperature": 0.5,
    "top_k": 250,
    "top_p": 1,
    "stop_sequences": ["\n\nHuman"],
}

textgen_llm = Bedrock(model_id="anthropic.claude-v2", client=boto3_bedrock)
accept = "application/json"
contentType = "application/json"

# Create a prompt template that has multiple input variables
multi_var_prompt = PromptTemplate(
    input_variables=["customerServiceManager", "customerName", "feedbackFromCustomer"],
    template="""

Human: Create an apology email from the Service Manager {customerServiceManager} to {customerName} in response to the following feedback that was received from the customer: 
<customer_feedback>
{feedbackFromCustomer}
</customer_feedback>

Assistant:""",
)

# Pass in values to the input variables
prompt = multi_var_prompt.format(
    customerServiceManager="Bob",
    customerName="John Doe",
    feedbackFromCustomer="""Hello Bob,
     I am very disappointed with the recent experience I had when I called your customer support.
     I was expecting an immediate call back but it took three days for us to get a call back.
     The first suggestion to fix the problem was incorrect. Ultimately the problem was fixed after three days.
     We are very unhappy with the response provided and may consider taking our business elsewhere.
     """,
)

body = json.dumps(
    {
        "prompt": prompt,
        "max_tokens_to_sample": inference_modifier["max_tokens_to_sample"],
        "temperature": inference_modifier["temperature"],
        "top_k": inference_modifier["top_k"],
        "top_p": inference_modifier["top_p"],
        "stop_sequences": inference_modifier["stop_sequences"],
    }
)

try:

    response = boto3_bedrock.invoke_model(
        body=body,
        modelId=textgen_llm.model_id,
        accept=accept,
        contentType=contentType,
    )
    response_body = json.loads(response.get("body").read())

    print(response_body.get("completion"))
    num_tokens = textgen_llm.get_num_tokens(prompt)
    print(f"Our prompt has {num_tokens} tokens")

except botocore.exceptions.ClientError as error:

    if error.response["Error"]["Code"] == "AccessDeniedException":
        print(
            f"\x1b[41m{error.response['Error']['Message']}\
                \nTo troubeshoot this issue please refer to the following resources.\
                 \nhttps://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_access-denied.html\
                 \nhttps://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html\x1b[0m\n"
        )

    else:
        raise error
