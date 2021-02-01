"""
 A main starting file
"""
from app.modules.hello import hello


def main():
    """
    The main entry point for the hello greeting app
    :return:
    """
    print('Enter your name:')
    name = input()
    print('Enter your language:')
    language = input()
    hello(name, language.lower())


if __name__ == "__main__":
    main()
