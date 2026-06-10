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

dotenv.load_dotenv()

# 编排prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是KIMI开发的聊天机器人，请回答用户的问题，现在的时间是{now}"),
        ("human", "{query}")
    ]
).partial(now=datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'))

chat = ChatOpenAI(
    model="kimi-k2.6",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),

)
stream = chat.stream(prompt.invoke({"query": "你能讲一下塞尔达与原神的区别吗"}))
for message in stream:
    print(message.content, flush=True, end="")
