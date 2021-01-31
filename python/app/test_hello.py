"""
THis modeule will handle all hello function testing
"""
import pytest

from hello import hello

name_test_data = [("Brian", "English", "Hello, Brian!"),
                  ("", "English", "Hello, World!")]


@pytest.mark.parametrize("name, language, want", name_test_data)
def test_hello_name(name: str, language: str, want: str):
    got: str = hello(name, language)
    assert got == want


langauge_test_data = [("Brian", "English", "Hello, Brian!"),
                      ("Brian", "", "Hello, Brian!"),
                      ("", "Hebrew", "Shalom, World!"),
                      ("", "Spanish", "Hola, World!")]


@pytest.mark.parametrize("name, language, want", langauge_test_data)
def test_hello_language(name: str, language: str, want: str):
    got: str = hello(name, language)
    assert got == want
