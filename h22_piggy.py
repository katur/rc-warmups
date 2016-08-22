'''Write a function that takes a string and encodes it in pig latin. Move all
consonants at the beginning of each word to the end, and if it then ends in a
consonant, append 'ay'.

E.g.
piggy('This is a string, yeah?') -> 'Isthay isay a ingstray, eahyay?'

y is always a consonant, and you should capitalize any words that were
capitalized in the original.
'''

import re
from itertools import groupby

VOWELS = 'aeiouAEIOU'
VOWELS_RE = r'[' + VOWELS + ']'


def piggy(s):
    out = ''

    for word in get_alpha_group(s):
        word = move_consonants_to_end(word)
        word = append_ay(word)
        out += word

    return out


def get_alpha_group(s):
    for k, group in groupby(s, str.isalpha):
        yield ''.join(list(group))


def move_consonants_to_end(word):
    first_vowel = re.search(VOWELS_RE, word)
    if first_vowel:
        index = first_vowel.start()
        word = word[index:] + word[0:index]

    return word


def append_ay(word):
    if is_consonant(word[-1]):
        word += 'ay'

    return word


def is_consonant(char):
    return char.isalpha() and char not in VOWELS


def is_vowel(char):
    return char in VOWELS


if __name__ == '__main__':
    print piggy('This is a string, yeah? wtf')
