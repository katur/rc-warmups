'''Write a function that takes a base word and a dictionary (a set of words).
Return all the words in the dictionary that can be made with one transformation
(adding, removing, or substituting a character) to the base word.

E.g.
link("race", miriamwebster)
-> {"ace", "brace", "rack", ...}
'''

import string

LETTERS = string.lowercase


def link(base, dictionary):
    results = set()
    results |= find_removes(base, dictionary)
    results |= find_adds(base, dictionary)
    results |= find_subs(base, dictionary)
    return results


def find_removes(base, dictionary):
    return {remove(base, i) for i in range(len(base))
            if remove(base, i) in dictionary}


def find_adds(base, dictionary):
    results = set()
    for letter in LETTERS:
        results |= {add(base, i, letter) for i in range(len(base))
                    if add(base, i, letter) in dictionary}
    return results


def find_subs(base, dictionary):
    results = set()
    for letter in LETTERS:
        results |= {sub(base, i, letter) for i in range(len(base))
                    if sub(base, i, letter) in dictionary}
    return results


def remove(base, i):
    return base[0:i] + base[i+1:]


def add(base, i, letter):
    return base[0:i] + letter + base[i:]


def sub(base, i, letter):
    return base[0:i] + letter + base[i+1:]


def load_words():
    """Return a set of words from  UNIX words file."""
    words = set()
    with open('/usr/share/dict/words', 'r') as f:
        for line in f:
            words.add(line.strip())
    return words


if __name__ == '__main__':
    words = load_words()
    print link('race', words)
