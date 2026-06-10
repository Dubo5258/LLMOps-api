# encoding=utf-8
"""
@author = db3343891468@163.com

{DATE} {TIME}
"""
import os

from flask import Flask

from internal.model.app import App
from internal.router import Router
from config import Config
from internal.exception import CustomException
from pkg.response import json, Response, HttpCode
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


class HTTP(Flask):
    def __init__(self, *args, conf: Config, db: SQLAlchemy, migrate: Migrate, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        """初始化应用配置"""
        self.config.from_object(conf)

        """"配置扩展模块"""
        db.init_app(self)
        migrate.init_app(self, db, directory="internal/migrations")

        """配置中文转义"""
        self.json.ensure_ascii = False

        """注册绑定异常错误处理"""
        self.register_error_handler(Exception, self._register_error_handler)

        """注册应用配置"""
        router.register_router(self)

    def _register_error_handler(self, error: Exception):
        """ 先判断是否为自定义异常"""
        if isinstance(error, CustomException):
            return json(Response(
                code=error.code,
                message=error.message,
                data=error.data,
            ))

        if self.debug or os.getenv("Flask_ENV") == "development":
            raise error
        else:
            return json(Response(
                code=HttpCode.FAIL,
                message=str(error),
                data={},
            ))
