'''Write a function that, given a positive integer, returns the number of ones
in the number's binary representation.

E.g.    ones(8) -> 1
        ones(7) -> 3
'''


def ones(number):
    binary = bin(number)[2:]
    return len([x for x in binary if x == '1'])


if __name__ == '__main__':
    print ones(8)
    print ones(7)
