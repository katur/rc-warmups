'''Write a function that returns a boolean indicating if a number is a happy
number. To do this:

    1) Replace it with the sum of the squares of its digits
    2) Repeat

If this process ends with 1, the number is happy; if this process gets stuck in
a loop, it's not.

E.g.
happy(19) -> True
happy(11) -> False
'''

MAX_ITERATION = 500


def happy(num):
    return happy_recursive(num, 0)


def happy_recursive(num, iteration):
    if num == 1:
        return True

    if iteration >= MAX_ITERATION:
        return False

    num = sum([int(i) * int(i) for i in str(num)])
    return happy_recursive(num, iteration + 1)


if __name__ == '__main__':
    print happy(19)
    print happy(11)
