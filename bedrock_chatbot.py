## Chatbot (Basic - without context)


import boto3
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.llms.bedrock import Bedrock
from labutils import print_ww

boto3_bedrock = boto3.client("bedrock-runtime")

chatbot_llm = Bedrock(model_id="ai21.j2-ultra-v1", client=boto3_bedrock)
memory = ConversationBufferMemory()
conversation_chain = ConversationChain(llm=chatbot_llm, verbose=True, memory=memory)

try:
    print_ww(conversation_chain.predict(input="Hi!"))
    print_ww(
        conversation_chain.predict(
            input="Give me a few tips on how to start a new garden."
        )
    )
    print_ww(conversation_chain.predict(input="Cool. Will that work with tomatoes?"))
    print_ww(conversation_chain.predict(input="That's all, thank you!"))

except ValueError as error:
    if "AccessDeniedException" in str(error):
        print(
            f"\x1b[41m{error}\
        \nTo troubeshoot this issue please refer to the following resources.\
         \nhttps://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_access-denied.html\
         \nhttps://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html\x1b[0m\n"
        )

        class StopExecution(ValueError):
            def _render_traceback_(self):
                pass

        raise StopExecution
    else:
        raise error
