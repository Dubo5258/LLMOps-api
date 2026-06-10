# encoding=utf-8
"""
@author = db3343891468@163.com

{DATE} {TIME}
"""
import os
import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

dotenv.load_dotenv()
prompt = ChatPromptTemplate.from_template("{query}")
chat = ChatOpenAI(
    model="kimi-k2.6",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),

)

parser = StrOutputParser()

chain = prompt | chat | parser
print(chain.invoke({"query": "你好，你是谁"}))
