# encoding=utf-8
"""
@author = db3343891468@163.com

{DATE} {TIME}
"""
import pytest

from app.llm.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
