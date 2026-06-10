# encoding=utf-8
"""
@author = db3343891468@163.com

{DATE} {TIME}
"""

from dataclasses import field, dataclass, is_dataclass, asdict
from enum import Enum
from typing import Any

from flask import jsonify

from .http_code import HttpCode


@dataclass
class Response:
    """基础HTTP响应风格"""
    code: HttpCode = HttpCode.SUCCESS
    message: str = ""
    data: Any = field(default_factory=dict)


def _to_jsonable(value: Any):
    if value is None:
        return None
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Response):
        return {
            "code": _to_jsonable(value.code),
            "message": value.message,
            "data": _to_jsonable(value.data),
        }
    if is_dataclass(value):
        return _to_jsonable(asdict(value))
    if isinstance(value, dict):
        return {str(k): _to_jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_to_jsonable(v) for v in value]
    return value


def json(data: Any = None, status_code: int = 200):
    return jsonify(_to_jsonable(data)), status_code


def SUCCESS(data: Any = None, message: str = "操作成功"):
    """成功响应"""
    response_obj = Response(code=HttpCode.SUCCESS, message=message, data=data)
    return json(response_obj)


def FAIL(data: Any = None, message: str = "操作失败"):
    """通用失败响应"""
    response_obj = Response(code=HttpCode.FAIL, message=message, data=data)
    return json(response_obj)


def NOT_FOUND(data: Any = None, message: str = "请求的资源不存在"):
    """资源未找到响应"""
    response_obj = Response(code=HttpCode.NOT_FOUND, message=message, data=data)
    return json(response_obj)


def UNAUTHORIZED(data: Any = None, message: str = "未授权，请先登录"):
    """未授权响应"""
    response_obj = Response(code=HttpCode.UNAUTHORIZED, message=message, data=data)
    return json(response_obj)


def FORBIDDEN(data: Any = None, message: str = "无权限访问该资源"):
    """无权限响应"""
    response_obj = Response(code=HttpCode.FORBIDDEN, message=message, data=data)
    return json(response_obj)


def VALIDATION_ERROR(data: Any = None, message: str = "数据验证错误"):
    """参数校验失败响应"""
    response_obj = Response(code=HttpCode.VALIDATION_ERROR, message=message, data=data)
    return json(response_obj)
