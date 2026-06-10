# encoding=utf-8
"""
@author = db3343891468@163.com

{DATE} {TIME}
"""
from flask_sqlalchemy import SQLAlchemy
from injector import Module, Binder
from flask_migrate import Migrate
from internal.extension.migrate_extension import migrate

from internal.extension.database_extension import db

"""扩展模块的依赖注入"""


class ExtensionModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)
        binder.bind(Migrate, to=migrate)
