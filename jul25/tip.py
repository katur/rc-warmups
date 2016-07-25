'''Write a function that takes a bill, along with a list of the diners'
suggested tips, and calculates the amount to be tipped (by taking the average
of the suggested tips and applying it to the bill).

bill is in dollars; suggested tips are percentages.

E.g. tip(100, [15, 20, 10, 10, 10, 25]) -> 15
'''


def average(l):
    if l:
        return float(sum(l)) / len(l)
    return None


def tip(bill, tips):
    tip = average(tips)
    return bill * tip / 100


if __name__ == '__main__':
    print tip(100, [15, 20, 10, 10, 10, 25])
    print tip(200, [20, 22, 18, 17.5, 22.5])
