import boto3
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory  # noqa: F811

# from labutils import chatux
from labutils import print_ww


boto3_bedrock = boto3.client("bedrock-runtime")

chatbot_llm = Bedrock(model_id="ai21.j2-ultra-v1", client=boto3_bedrock)
memory = ConversationBufferMemory()
memory.chat_memory.add_user_message(
    "Context:You will be acting as a career coach. Your goal is to give career advice to users"
)
memory.chat_memory.add_ai_message("I am career coach and give career advice")

# turn verbose to true to see the full logs and documents
conversation = ConversationChain(
    llm=chatbot_llm, verbose=False, memory=memory  # memory_chain
)

print_ww(conversation.predict(input="What are the career options in AI?"))

conversation.verbose = False
print_ww(conversation.predict(input="How to fix my car?"))

# This code part work on Jupityer Notebook
# chat = chatux.ChatUX(conversation)
# chat.start_chat()
