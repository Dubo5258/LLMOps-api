# encoding=utf-8
"""
@author = db3343891468@163.com

{DATE} {TIME}
"""
import datetime
import os
import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
dotenv.load_dotenv()
# 编排prompt
prompt = ChatPromptTemplate.from_template("{query}")

parse = StrOutputParser()

chat = ChatOpenAI(
    model="kimi-k2.6",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),

)
res = parse.invoke(chat.invoke(
    prompt.invoke({
        "query": "现在是几点，请给我讲一下有关原神的游戏"
    })
))
print(res)
