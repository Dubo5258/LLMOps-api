# encoding=utf-8
"""
@author = db3343891468@163.com

{DATE} {TIME}
"""
import pytest

from pkg.response import HttpCode


class TestAppHandler:
    """app控制器测试"""

    @pytest.mark.parametrize("query", [None, "你好"])
    def test_completion(self, query, client):
        response = client.post('/app/completion', json={"query": query})

        assert response.status_code == 200
        if query is not None:
            assert response.json.get('code') == HttpCode.SUCCESS

        else:
            assert response.json.get('code') == HttpCode.VALIDATION_ERROR
        print("内容:", response.json)
