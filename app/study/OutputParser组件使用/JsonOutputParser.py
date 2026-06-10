# encoding=utf-8
"""
@author = db3343891468@163.com

{DATE} {TIME}
"""
import os

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

dotenv.load_dotenv()


class Joke(BaseModel):
    joke: str = Field(description="回答用户的疑问")
    joke1: str = Field(description="向用户推荐有关其他的知识")


chat = ChatOpenAI(
    model="kimi-k2.6",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),

)
parser = JsonOutputParser(pydantic_object=Joke)

prompt = ChatPromptTemplate.from_template(template="请根据用户问题来回答, \n{format_instructions}\n{query}",
                                          partial_variables={'format_instructions': parser.get_format_instructions()})

joke = parser.invoke(chat.invoke(prompt.invoke({"query": "你是谁"})))
print(joke)
