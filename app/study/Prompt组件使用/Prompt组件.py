# encoding=utf-8
"""
@author = db3343891468@163.com

{DATE} {TIME}
"""
import datetime

from langchain_core.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)


prompts = PromptTemplate.from_template("请讲一个有关{subject}的故事")
print(prompts.format(subject="原神"))

chat_prompts = ChatPromptTemplate.from_messages(
    [
        ("system", "你是机器人,请回答用户提问的问题，现在时间为{now}"),
        # 有时可能还有其他消息，不一定
        MessagesPlaceholder("chat_history"),
        HumanMessagePromptTemplate.from_template("请讲一个有关{subject}的故事")
    ]
)

chat_prompts_value = chat_prompts.invoke({
    "chat_history": [
        ("human", "我叫小杜")
    ],
    "now": datetime.datetime.now(),
    "subject": "程序员"
})

print(chat_prompts_value.to_string())