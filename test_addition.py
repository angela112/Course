import pytest
from addition import add

def test_add():
    assert add(1, 2) == 3   # 测试用例1
    assert add(-1, 1) == 0  # 测试用例2
    assert add(0, 0) == 0   # 测试用例3
