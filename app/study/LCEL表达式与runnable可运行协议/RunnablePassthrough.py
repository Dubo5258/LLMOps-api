# encoding=utf-8
"""
@author = db3343891468@163.com

{DATE} {TIME}
"""
import os
from operator import itemgetter

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnablePassthrough

dotenv.load_dotenv()


def retrieval(query: str) -> str:
    print("正在检索...", query)
    return "我是小杜"


prompt = ChatPromptTemplate.from_template(
    """请根据用户的问题来回复，可以参考对应的上下文
    <context>
    {context}
    </context>
    用户的问题是：{query}
    """
)

chat = ChatOpenAI(
    model="kimi-k2.6",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),

)

parser = StrOutputParser()
res = RunnablePassthrough.assign(context=lambda x: retrieval(x['query'])) | prompt | chat | parser

cont = res.invoke({"query": "你好，我是谁？"})
print(cont)
