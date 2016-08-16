'''Write a function that takes two strings, and checks whether the letters of
the first one appear in order (but not necessarily adjacent in the second).

fuzzy('abc', 'a baby cat') -> True
fuzzy('abc', 'acbb') -> False
fuzzy('', '') -> True
fuzzy('', 'abc') -> True
fuzzy('abc', '') -> False
'''


def fuzzy_recursive(a, b, a_i, b_i):
    """
    Strings are a and b; current indices into strings are a_i, b_i
    """
    # We have found all the letters of a in b
    if a_i == len(a):
        return True

    # We reached end of b without finding all the letters of a
    if b_i == len(b):
        return False

    # We found the next letter of a, so increment a
    if a[a_i] == b[b_i]:
        a_i += 1

    # Increment b
    b_i += 1
    return fuzzy_recursive(a, b, a_i, b_i)


def fuzzy(a, b):
    return fuzzy_recursive(a, b, 0, 0)


if __name__ == '__main__':
    print fuzzy('abc', 'a baby cat')
    print fuzzy('abc', 'acbb')
    print fuzzy('', '')
    print fuzzy('', 'abc')
    print fuzzy('abc', '')
