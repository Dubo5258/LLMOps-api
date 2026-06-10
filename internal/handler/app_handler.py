# encoding=utf-8
"""
@author = db3343891468@163.com

{DATE} {TIME}
"""
import os
import uuid
from dataclasses import dataclass

from flask import request
from injector import inject
from openai import OpenAI
from internal.schema.app_schema import CompletionReq
from internal.exception import FailException
from internal.service import AppService
from pkg.response import HttpCode
from pkg.response.response import (SUCCESS, FAIL, FORBIDDEN, NOT_FOUND, VALIDATION_ERROR)
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


@inject
@dataclass
class AppHandler:
    """  应用控制器  """
    app_service: AppService

    def create_app(self):
        """添加app数据"""
        app = self.app_service.create_app()
        return SUCCESS(message=f"应用已经创建，ID为：{app.id}")

    def get_app(self, id: uuid.UUID):
        app = self.app_service.get_app(id)
        if app is None:
            return NOT_FOUND()
        return SUCCESS(message=f"应用已经成功获取，ID为{app.id}")

    def update_appName(self, id: uuid.UUID):
        app = self.app_service.update_appName(id)
        if app is None:
            return NOT_FOUND()
        return SUCCESS(message=f"ID为：{app.id} 的应用名字已经修改为：{app.name}")

    def delete_app(self, id: uuid.UUID):
        app = self.app_service.delete_app(id)
        if app is None:
            return NOT_FOUND()
        return SUCCESS(message=f"ID为{app.id}的{app.name}应用已经删除成功")

    def debug(self, app_id: uuid.UUID):
        """聊天接口"""

        """"数据校验"""
        req = CompletionReq()
        if not req.validate():
            return VALIDATION_ERROR(data=req.errors)
        # 提示词模板
        prompt = ChatPromptTemplate.from_template("{query}")
        # 构造OpenAI客户端，发起请求
        chat = ChatOpenAI(
            model="kimi-k2.6",
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_API_BASE"),

        )
        # 构造输出解析器
        praser = StrOutputParser()

        chain = prompt | chat | praser
        content = chain.invoke({"query": req.query.data})
        return SUCCESS(data={"answer": content})

    def ping(self):
        raise FailException("数据未找到")
        # return {'message': 'pong'}
