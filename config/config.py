# encoding=utf-8
"""
@author = db3343891468@163.com

{DATE} {TIME}
"""
import os
from typing import Any
from .default_config import DEFAULT_CONFIG


def _get_env(key: str) -> Any:
    """从环境变量中获取配置，默认配置来补全"""
    return os.getenv(key, DEFAULT_CONFIG.get(key))


def _get_bool_ebv(key: str) -> bool:
    """从环境变量中获取bool配置，默认配置来补全"""
    value: str = _get_env(key)
    return value.lower() == 'true' if value is not None else False


class Config:
    def __init__(self):
        self.WTF_CSRF_ENABLED = _get_bool_ebv('WTF_CSRF_ENABLED')

        """数据库配置"""

        self.SQLALCHEMY_DATABASE_URI = _get_env('SQLALCHEMY_DATABASE_URI')
        self.SQLALCHEMY_ENGINE_OPTIONS = {
            "pool_size": _get_env('SQLALCHEMY_POOL_SIZE'),
            "pool_recycle": _get_env('SQLALCHEMY_POOL_RECYCLE'),
        }
        self.SQLALCHEMY_ECHO = True
