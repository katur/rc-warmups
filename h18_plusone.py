'''Write a function that takes a string and increments all the numbers that
appear in it.

E.g.
plusone("1+15=16") -> "2+16=17"
plusone("call me at 3.555-2020") -> "call me at 4.555-2019"
'''

import re

NUMBER = '-?\d+\.?\d*'


def increment_replace(matchobj):
    s = matchobj.group(0)

    try:
        num = int(s)
    except ValueError:
        num = float(s)

    num += 1
    return str(num)


def plusone(s):
    return re.sub(NUMBER, increment_replace, s)


if __name__ == '__main__':
    print plusone('1+15=16')
    print plusone('call me at 3.555-2020')
