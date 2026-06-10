# encoding=utf-8
"""
@author = db3343891468@163.com

{DATE} {TIME}
"""
# 应用默认配置项

DEFAULT_CONFIG = {

    # csef配置
    'WTF_CSRF_ENABLED': "False",
    # 数据库配置
    "SQLALCHEMY_DATABASE_URI": "postgresql://postgres:postgres@localhost:54321/postgres?client_encoding=utf8",
    "SQLALCHEMY_POOL_SIZE": 30,
    "SQLALCHEMY_POOL_RECYCLE": 3600,
    "SQLALCHEMY_ECHO": "True"
}