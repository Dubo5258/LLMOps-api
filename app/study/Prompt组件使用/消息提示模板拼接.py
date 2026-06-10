# encoding=utf-8
"""
@author = db3343891468@163.com

{DATE} {TIME}
"""
from langchain_core.prompts import (
    ChatPromptTemplate
)

system_chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是机器人，请根据用户的问题回答，我叫{username}")
])

human_chat_prompt = ChatPromptTemplate.from_messages([
    ("human", "{query}")
])

chat_prompt = system_chat_prompt + human_chat_prompt

print(chat_prompt.invoke({
    "username": "小杜",
    "query": "你好你是"
}).to_string())
