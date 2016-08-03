'''Our removing all vowels compression scheme made so much money in Hawaii that
the studeio has bought as sequel. This time, we're going to read a file, and
remove the first and last letters of all words that are 3 letters or more. A
word is any adjacent series of letters.

lc2("annakarenina.txt")
"All app amile are like, ac nhapp ..."
'''

import re


def lc2(filename):
    with open(filename, 'r') as f:
        for line in f:
            # Avoid \w because it includes digits and underscore
            print re.sub(r'[a-zA-Z]([a-zA-Z]{2,})[a-zA-Z]', r'\1',
                         line.rstrip())


if __name__ == '__main__':
    lc2('annakarenina.txt')
