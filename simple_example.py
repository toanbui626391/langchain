from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

"""
Example of how to use langchain to connect with openai model and use it to predict result
"""
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(openai_api_key=api_key)

result = chat_model.predict("hi!")
print(result)