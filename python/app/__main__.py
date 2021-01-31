"""
 A main starting file 
"""
from hello import hello


def main():
    print('Enter your name:')
    name = input()
    print('Enter your language:')
    language = input()
    hello(name, language.lower())


if __name__ == "__main__":
    main()
