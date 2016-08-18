'''Write a function that takes a list of letters and returns a
hash/dict/association list/whatever of characters with the number of times they
appear in the input
abbacdeb
a-2  b-3 ...
'''


def count(l):
    d = {}
    for item in l:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1
    return d


if __name__ == '__main__':
    print count('abbacdeb')
