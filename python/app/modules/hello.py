"""
This module will hold all hello related code
"""
from typing import Optional


def hello(name: Optional[str], language: Optional[str]) -> str:
    """
    This is the hello function that will greet users.

        name: the name to use as a greeting, if none given then World is used.

    :return:
    """
    if not name:
        name = "World"
    if not language:
        greeting = "Hello"
    if language == "english":
        greeting = "Hello"
    elif language == "spanish":
        greeting = "Hola"
    elif language == "hebrew":
        greeting = "Shalom"
    return f"{greeting}, {name}!"
