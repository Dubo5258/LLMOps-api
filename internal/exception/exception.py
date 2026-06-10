# encoding=utf-8
"""
@author = db3343891468@163.com

{DATE} {TIME}
"""
from dataclasses import field
from typing import Any
from pkg.response import HttpCode


class CustomException(Exception):
    """基础自定义异常信息"""

    code: HttpCode = HttpCode.FAIL
    message: str = ""
    data: Any = field(default_factory=dict)

    def __init__(self, message: str = None, data: Any = None):
        super().__init__()
        self.message = message
        self.data = data


class FailException(CustomException):
    pass


class NotFoundException(CustomException):
    code = HttpCode.NOT_FOUND


class UnauthorizedException(CustomException):
    code = HttpCode.UNAUTHORIZED


class ForbiddenException(CustomException):
    code = HttpCode.FORBIDDEN


class ValidationException(CustomException):
    code = HttpCode.VALIDATION_ERROR
