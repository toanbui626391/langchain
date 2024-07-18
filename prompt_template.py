from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from dotenv import load_dotenv
import os


"""
Example of using ChatPromptTemplate object 
"""
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(openai_api_key=api_key)

#template is what openai will do or acting, 
#define template with variable which can change
template = "You are a helpful assistant that translates {input_language} to {output_language}."
human_template = "{text}" #input or query from human

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

messages = chat_prompt.format_messages(input_language="English", 
                                        output_language="French", 
                                        text="I love programming.")
result = chat_model.predict_messages(messages)
print(result.content)