'''Given a list/dict of number:string pairs, print out the numbers up to 100
with replacements as in fizzbuzz.

E.g. ff({2:'hi', 3:'world', 4:'!'})

1
hi
world
hi!
5
hiworld
7
hi!
world
hi
11
hiworld!
13
...
'''


def ff(pairs):
    for i in range(1, 101):
        s = ''.join(word for key, word in pairs.iteritems() if not i % key)
        print s if s else str(i)


if __name__ == '__main__':
    ff({2: 'hi', 3: 'world', 4: '!'})
