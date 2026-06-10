# encoding=utf-8
"""
@author = db3343891468@163.com

{DATE} {TIME}
"""
import os

from injector import Injector
from app.llm.module import ExtensionModule
from internal.router import Router
from internal.server import HTTP
from config import Config
import dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

dotenv.load_dotenv()
conf = Config()

injector = Injector([ExtensionModule])

app = HTTP(__name__, conf=conf, db=injector.get(SQLAlchemy), migrate=injector.get(Migrate), router=injector.get(Router))

if __name__ == '__main__':
    app.run(debug=True)
