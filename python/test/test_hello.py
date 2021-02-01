"""
THis modeule will handle all hello function testing
"""
import pytest

from app.modules.hello import hello

NAME_TEST_DATA = [("Brian", "English", "Hello, Brian!"),
                  ("", "English", "Hello, World!")]


@pytest.mark.parametrize("name, language, want", NAME_TEST_DATA)
def test_hello_name(name: str, language: str, want: str):
    """
    This test is related to teh name argument
    :param name:  What name to greet, blank is defaulted to Word.
    :param language:
    :param want:
    :return:
    """
    got: str = hello(name, language)
    assert got == want


LANGUAGE_TEST_DATA = [("Brian", "english", "Hello, Brian!"),
                      ("Brian", "", "Hello, Brian!"),
                      ("", "hebrew", "Shalom, World!"),
                      ("", "spanish", "Hola, World!")]


@pytest.mark.parametrize("name, language, want", LANGUAGE_TEST_DATA)
def test_hello_language(name: str, language: str, want: str):
    """
       This test is related to teh name argument
       :param name:
       :param language: What language to greet with, english is the default.
       :param want:
       :return:
       """
    got: str = hello(name, language)
    assert got == want
