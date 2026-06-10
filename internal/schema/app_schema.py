# encoding=utf-8
"""
@author = db3343891468@163.com

{DATE} {TIME}
"""
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    """ 基础聊天请求验证 """
    query = StringField('query', validators=[
        DataRequired("用户的提问不能为空"),
        Length(max=2000, message="用户的问题最大长度不能超过2000"),
    ])
