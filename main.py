#! /usr/bin/python
from googletrans import Translator
import sys


def main():
    to_translate = ''
    if len(sys.argv) < 2:
        to_translate = input("Enter text to translate: ")
    else:
        to_translate = ' '.join(sys.argv[1:])

    translator = Translator()
    translated = translator.translate(to_translate, dest='zh-cn')
    print(translated.text)
    print(translated.pronunciation)


if __name__ == '__main__':
    main()
