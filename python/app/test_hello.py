"""
THis modeule will handle all hello function testing
"""
import pytest

from hello import hello

TESTDATA = [("Brian", "Hello, Brian!"),
            ("", "Hello, World!")]


@pytest.mark.parametrize("name, want", TESTDATA)
def test_hello(name: str, want: str):
    got: str = hello(name)
    assert got == want
