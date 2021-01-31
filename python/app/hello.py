"""
This module will hold all hello related code
"""
from typing import Optional


def hello(name: Optional) -> str:
    """
    This is the hello function that will greet users.

        name: the name to use as a greeting, if none given then World is used.

    :return:
    """
    if not name:
        name = "World"
    return f"Hello, {name}!"
