'''Given a string, find the first non-repeating character in it and return its
index. Return -1 if there is no non-repeating char.

E.g.
firstunique('aabcc') -> 2
firstunique('aabbcc') -> -1
'''

from collections import OrderedDict


def firstunique(s):
    counts = OrderedDict()

    for char in s:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1

    for k, v in counts.iteritems():
        if v == 1:
            return s.index(k)

    return -1


if __name__ == '__main__':
    print firstunique('aabcc')
    print firstunique('aabbcc')
