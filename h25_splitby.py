'''Write a function that takes a filename and a list of words, and returns a
list of strings that appear in the file between occurrences of the words in the
list.

E.g.
splitby('foo.txt', ['am', 'is']) -> [
    'this',
    'an\nexample- I\n',
    'excited!'
]

foo.txt
    this is an
    example- I
    am excited!
'''

import re


def splitby(filename, l):
    pattern = '|'.join('\s' + i + '\s' for i in l)

    with open(filename, 'r') as f:
        return re.split(pattern, f.read())


if __name__ == '__main__':
    print splitby('h25_foo.txt', ['am', 'is'])
