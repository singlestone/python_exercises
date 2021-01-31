"""
THis modeule will handle all hello function testing
"""
from hello import hello


def test_hello():
    got: str = hello()
    want: str = "Hello, World!"
    assert want == got
