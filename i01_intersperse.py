'''Write a function that takes a list of lists and intersperses their elements.

E.g.
intersperse([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) => [1, 4, 7, 2, 5, 8, 3, 6, 9]
'''


def get_next_element(l):
    index = 0
    while index < len(l[0]):
        for sublist in l:
            yield sublist[index]
        index += 1


def intersperse(l):
    return [i for i in get_next_element(l)]


if __name__ == '__main__':
    print intersperse([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
