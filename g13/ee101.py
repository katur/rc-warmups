'''In electronics, V=IR (voltage = current * resistance). Write a function
that can take any 2 of these values and calculates the third.

E.g. ee101({v:6, r:2}) -> {i:3}

By Emily and Katherine
'''

from __future__ import division


def ee101_keywords(v=None, i=None, r=None):
    if v is None:
        return i * r
    else:
        return v / (i or r)


def ee101_simple(d):
    if 'v' not in d:
        return {'v': d['i'] * d['r']}
    elif 'i' not in d:
        return {'i': d['v'] / d['r']}
    else:
        return {'r': d['v'] / d['i']}


def ee101_absurd(d):
    if 'v' not in d:
        return {'v': d['i'] * d['r']}
    else:
        possibilities = 'ir'
        present = [key for key in d.keys() if key is not 'v'][0]
        absent = (possibilities.find(key) + 1) % 2
        return {absent: d['v'] / d[present]}


if __name__ == '__main__':
    print ee101_simple({'v': 6, 'r': 2})
    print ee101_simple({'r': 3, 'i': 4})
    print ee101_absurd({'v': 6, 'r': 2})
    print ee101_absurd({'r': 3, 'i': 4})
    print ee101_keywords(v=6, r=2)
    print ee101_keywords(r=3, i=4)
