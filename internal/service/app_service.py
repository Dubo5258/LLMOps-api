# encoding=utf-8
"""
@author = db3343891468@163.com

{DATE} {TIME}
"""
import uuid

from injector import inject
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

from internal.model.app import App


@inject
@dataclass
class AppService:
    """应用服务逻辑"""
    db: SQLAlchemy

    def create_app(self) -> App:
        with self.db.session.begin():
            #创建模型的实体类
            app = App()
            app.account_id = uuid.uuid4()
            app.name = "测试机器人"
            app.icon = ""
            app.description = "简单机器人"
            #将实体类添加到会话中
            self.db.session.add(app)

            return app

    def get_app(self, id: uuid.UUID) -> App:
        app = self.db.session.query(App).get(id)
        return app

    def update_appName(self, id: uuid.UUID) -> App:
        with self.db.session.begin():
            app = self.get_app(id)
            app.name = "原神"
            return app

    def delete_app(self, id: uuid.UUID) ->App:
        with self.db.session.begin():
            app = self.get_app(id)
            self.db.session.delete(app)
            return app

