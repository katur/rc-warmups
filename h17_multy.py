'''Write a function that takes 2 numbers, and returns the smallest prefix of
the 2nd that is a multiple of the 1st.

E.g.
multy(8, 216500) -> 216
multy(5, 1234) -> None
'''

TEN = 10


def multy(a, b):
    # Get b rounded down to the nearest tens-place
    power = len(str(b)) - 1

    if str(b)[0] == '-':
        power -= 1

    place = pow(TEN, power)

    while place >= 1:
        prefix = b // place
        if prefix % a == 0:
            return prefix
        place /= TEN

    return None


if __name__ == '__main__':
    print multy(8, 216500)  # 216
    print multy(5, 1234)    # None
    print multy(7, 7234)    # 7
    print multy(-1, -1)     # -1
    print multy(-5, -25)    # -25
    print multy(-5, 1003)   # 10
    print multy(-5, -14)    # None
