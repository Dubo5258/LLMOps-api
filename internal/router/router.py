# encoding=utf-8
"""
@author = db3343891468@163.com

{DATE} {TIME}
"""
from injector import inject
from flask import Flask, Blueprint
from internal.handler import AppHandler
from dataclasses import dataclass


@inject
@dataclass
class Router:
    app_handler: AppHandler

    def register_router(self, app: Flask):
        bp = Blueprint('llmOps', __name__, url_prefix='')
        # bp.add_url_rule("/ping", view_func=self.app_handler.ping)
        bp.add_url_rule("/app/<uuid:api_ia>/debug", methods=["POST"], view_func=self.app_handler.debug)
        # bp.add_url_rule("/app", methods=["POST"],view_func=self.app_handler.create_app)
        # bp.add_url_rule("/app/<id>", view_func=self.app_handler.get_app)
        # bp.add_url_rule("/app/<id>", methods=["POST"], view_func=self.app_handler.update_appName)
        # bp.add_url_rule("/app/<id>/delete", methods=["POST"], view_func=self.app_handler.delete_app)
        # 注册蓝图
        app.register_blueprint(bp)


