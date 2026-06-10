# encoding=utf-8
"""
@author = db3343891468@163.com

{DATE} {TIME}
"""
import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, Index, PrimaryKeyConstraint, String, Text
from sqlalchemy.dialects.postgresql import UUID

from internal.extension.database_extension import db


class App(db.Model):
    """应用配置表"""

    __tablename__ = 'app'

    # 复合表参数：定义主键和索引
    __table_args__ = (
        PrimaryKeyConstraint('id', name='app_pkey'),
        Index('idx_app_account_id', 'account_id'),  # 为 account_id 添加索引
    )

    # 主键：UUID 类型
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
        comment='主键 ID'
    )

    # 名称：字符串类型，默认空字符串
    name = Column(
        String(255),
        nullable=False,
        default="",
        comment='应用名称'
    )

    # 账户 ID：UUID 类型，带索引
    account_id = Column(
        UUID(as_uuid=True),
        nullable=False,
        comment='所属账户 ID'
    )

    # 图标：字符串类型
    icon = Column(
        String(255),
        nullable=False,
        default="",
        comment='应用图标 URL'
    )

    # 描述：长文本类型
    description = Column(
        Text,
        nullable=False,
        default="",
        comment='应用描述'
    )

    # 更新时间：自动更新
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.now,
        onupdate=datetime.now,
        comment='更新时间'
    )

    # 创建时间：仅初始化时赋值
    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.now,
        comment='创建时间'
    )
