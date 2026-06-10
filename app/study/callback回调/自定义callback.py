# encoding=utf-8
"""
@author = db3343891468@163.com

{DATE} {TIME}
"""
import os
from typing import Any
from uuid import UUID

import dotenv
from langchain_core.messages import BaseMessage
from langchain_core.outputs import GenerationChunk, ChatGenerationChunk
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.callbacks import StdOutCallbackHandler, BaseCallbackHandler

dotenv.load_dotenv()


class llmOps_callback_handler(BaseCallbackHandler):
    def on_chat_model_start(
            self,
            serialized: dict[str, Any],
            messages: list[list[BaseMessage]],
            *,
            run_id: UUID,
            parent_run_id: UUID | None = None,
            tags: list[str] | None = None,
            metadata: dict[str, Any] | None = None,
            **kwargs: Any,
    ) -> Any:
        print("模型开始执行：", serialized)
        print("messages:", messages)

    def on_llm_new_token(
            self,
            token: str,
            *,
            chunk: GenerationChunk | ChatGenerationChunk | None = None,
            run_id: UUID,
            parent_run_id: UUID | None = None,
            tags: list[str] | None = None,
            **kwargs: Any,
    ) -> Any:
        print("tokens成立：", token)


prompt = ChatPromptTemplate.from_template("{query}")
chat = ChatOpenAI(
    model="kimi-k2.6",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),

)

parser = StrOutputParser()

chain = {"query": RunnablePassthrough()} | prompt | chat | parser
res = chain.stream("你好，你是谁", config={'callbacks': [StdOutCallbackHandler(), llmOps_callback_handler()]})

for chunk in res:
    pass
