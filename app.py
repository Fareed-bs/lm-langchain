from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Connect to LM Studio API
llm = ChatOpenAI(
    model="llama-3.2-1b",
    openai_api_base="http://localhost:1234/v1",  # LM Studio API URL
    openai_api_key="lm-studio",  # Dummy key for OpenAI-compatible API
    streaming=True,  # Enable streaming
)

# User input
user_query = "Tell me about AI?"

# Stream response
print("AI Response: ", end="", flush=True)
for chunk in llm.stream([HumanMessage(content=user_query)]):
    print(chunk.content, end="", flush=True)

print()  # Add a newline after response
