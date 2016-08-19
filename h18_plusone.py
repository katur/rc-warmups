'''Write a function that takes a string and increments all the numbers that
appear in it.

E.g.
plusone("1+15=16") -> "2+16=17"
plusone("call me at 3.555-2020") -> "call me at 4.555-2019"
'''

import re

# This one requires a digit before the decimal point. Downside: .36 is
# captured as the integer 36 (so becomes .37)
# NUMBER = '-?(\d+\.?\d*)'

# This one requires a digit before or after the point. Downside: 36., at the
# end of a sentence, is perceived as a float (so becomes 37.0)
# NUMBER = '-?(\d+\.?\d*)|(\d*\.?\d+)'

# This one separates floats (with optional preceding digits) from integers
# (which are not followed by a decimal point).
NUMBER = '-?(\d*\.?\d+)|(\d+[^\.\d])'


def increment_replace(matchobj):
    s = matchobj.group(0)

    try:
        num = int(s)
    except ValueError:
        num = float(s)

    num += 1

    # Add back trailing 0s (might be nice for $5.00)
    # Do not bother with preceding 0s, since unclear how to handle case of
    # moving up by a tens-place; maybe this could be done with zfill.

    if '.' in s:
        padding = len(s.split('.')[1])
        return '{:.{padding}f}'.format(num, padding=padding)

    return str(num)


def plusone(s):
    return re.sub(NUMBER, increment_replace, s)


if __name__ == '__main__':
    print plusone('1+15=16')
    print plusone('call me at 3.555-2020')
    print plusone('My favorite number is 36.')
    print plusone('My favorite float is .36')
    print plusone('My favorite negative number is -36.')
    print plusone('My favorite negative float is -.36')
    print plusone('That costs $5.00?!')
