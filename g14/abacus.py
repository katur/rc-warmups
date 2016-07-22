'''Write a function that takes two strings representing numbers, and returns a
string representing their sum, *without* converting the strings to numbers -
use string operations only (you may convert the strings to lists of characters
if this is easier in your language).

E.g. abacus("32", "180") -> "212"
'''

TO_DASHES = {
    '0': '',
    '1': '-',
    '2': '--',
    '3': '---',
    '4': '----',
    '5': '-----',
    '6': '------',
    '7': '-------',
    '8': '--------',
    '9': '---------',
}

FROM_DASHES = {
    '': '0',
    '-': '1',
    '--': '2',
    '---': '3',
    '----': '4',
    '-----': '5',
    '------': '6',
    '-------': '7',
    '--------': '8',
    '---------': '9',
}


def abacus(x, y):
    x = x.zfill(len(y))
    y = y.zfill(len(x))

    solution = ''
    carry = '0'

    for (a, b) in zip(reversed(x), reversed(y)):
        dashed_sum, carry = add(a, b, carry)
        digit = FROM_DASHES[dashed_sum]
        solution = digit + solution

    if carry == '1':
        solution = '1' + solution

    return solution


def add(a, b, carry):
    '''Single digit case.

    Returns tuple (number, True) if should carry 1, (number, False) otherwise.
    '''
    dashes = TO_DASHES[a] + TO_DASHES[b] + TO_DASHES[carry]

    if len(dashes) <= 9:
        return (dashes, '0')
    else:
        ten_removed = dashes[:-10]
        return (ten_removed, '1')


if __name__ == '__main__':
    print abacus('32', '180')
    print abacus('998', '9999')
