import boto3
import botocore
import json
from langchain.llms.bedrock import Bedrock
from labutils import print_ww

boto3_bedrock = boto3.client("bedrock-runtime")

inference_modifier = {
    "max_tokens_to_sample": 4096,
    "temperature": 0.5,
    "top_k": 250,
    "top_p": 0.5,
    "stop_sequences": [],
}

textsumm_llm = Bedrock(model_id="anthropic.claude-v2", client=boto3_bedrock)
accept = "application/json"
contentType = "application/json"

prompt = """

Human: Please provide a summary of the following text.
<text>
AWS took all of that feedback from customers, and today we are excited to announce Amazon Bedrock, \
a new service that makes FMs from AI21 Labs, Anthropic, Stability AI, and Amazon accessible via an API. \
Bedrock is the easiest way for customers to build and scale generative AI-based applications using FMs, \
democratizing access for all builders. Bedrock will offer the ability to access a range of powerful FMs \
for text and images—including Amazons Titan FMs, which consist of two new LLMs we’re also announcing \
today—through a scalable, reliable, and secure AWS managed service. With Bedrock’s serverless experience, \
customers can easily find the right model for what they’re trying to get done, get started quickly, privately \
customize FMs with their own data, and easily integrate and deploy them into their applications using the AWS \
tools and capabilities they are familiar with, without having to manage any infrastructure (including integrations \
with Amazon SageMaker ML features like Experiments to test different models and Pipelines to manage their FMs at scale).
</text>

Assistant:"""

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
        modelId=textsumm_llm.model_id,
        accept=accept,
        contentType=contentType,
    )

    response_body = json.loads(response.get("body").read())
    print_ww(response_body.get("completion"))

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
