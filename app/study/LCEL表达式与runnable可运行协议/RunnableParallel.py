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
from langchain_core.runnables import RunnableParallel,RunnablePassthrough

dotenv.load_dotenv()
poem = ChatPromptTemplate.from_template("请将一个有关{query}的诗")
joke = ChatPromptTemplate.from_template("请讲一个有关{subject}的笑话")
chat = ChatOpenAI(
    model="kimi-k2.6",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),

)
parser = StrOutputParser()
joke_chain = joke | chat | parser
poem_chain = poem | chat | parser

map_chain = RunnableParallel({
    "joke": joke_chain,
    "poem": poem_chain,
})

map_chain.invoke({
    "query": "xxx",
    "subject": "xxx"
})
