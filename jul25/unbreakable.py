'''Write a function that takes a string and reverses every word in the string.
'Words' here means adjacent sets of letters in whatever alphabets you wish to
handle.

E.g. unbreakable("hello world.txt 123!") -> "olleh dlrow.txt 123!"
'''

import re


def unbreakable(s):
    return re.sub(r'[a-zA-Z]+', lambda x: x.group(0)[::-1], s)


if __name__ == '__main__':
    print unbreakable('hello world.txt 123!')
    print unbreakable('this is a sentence with 30 or so letters')
