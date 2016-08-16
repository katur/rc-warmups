'''Write a function that takes a recipe and a number n, and outputs
n times the recipe with appropriate unit conversions.

units
3t = 1T
16T = 1c
4c = 1q

example
tasty(2, {
    'mayonnaise': (2, 'c')
    'brown sugar': (8, 'T')
    'cayenne': (2, 't')})

-> {'mayonnaise: (1, 'q'),
    'brown sugar': (1, 'c'),
    'cayenne': (1.33... 'T')}
'''


# key = value[1] / value[0]
# i.e.
# key * value[0] = value[1]

# read as 3 't' per 'T'

CONVERT = {
    't': (3, 'T'),
    'T': (16, 'c'),
    'c': (4, 'q'),
}


def tasty(n, recipe):
    res = {}

    for ingredient, v in recipe.iteritems():
        amt, unit = v
        amt *= n
        res[ingredient] = convert(amt, unit)

    return res


def convert(amt, unit):
    # To take care of 'q', the largest unit, not being in the lookup table
    if unit not in CONVERT:
        return (amt, unit)

    conversion_amt, conversion_unit = CONVERT[unit]

    if amt < conversion_amt:
        return (amt, unit)

    converted_amt = float(amt) / conversion_amt
    return convert(converted_amt, conversion_unit)


if __name__ == '__main__':
    print tasty(2, {
        'mayonnaise': (2, 'c'),
        'brown sugar': (8, 'T'),
        'cayenne': (2, 't')}
    )
