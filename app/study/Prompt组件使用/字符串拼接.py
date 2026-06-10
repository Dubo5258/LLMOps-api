# encoding=utf-8
"""
@author = db3343891468@163.com

{DATE} {TIME}
"""
from langchain_core.prompts import PromptTemplate

prompt = (
    PromptTemplate.from_template("xxx")
    + ",xxxx",
    "\nxxxxx"
)
print(prompt)