'''You go into a very small grocery store with a fixed amount of money, wanting
to spend as much of your budget as possible on a single item. What will you be
eating this week, and how much of it can you afford?

E.g.
lifeskills(20.04, {'ketchup': 2.99, 'avocados': 0.99, 'milk': 3.25})
    => ('avocados', 20)  # leaving 24 cents
'''


def lifeskills(budget, prices):
    min_item = None
    min_change = None

    for item, price in prices.iteritems():
        change = budget % price
        if min_change is None or change < min_change:
            min_change = change
            min_item = (item, int(budget // price))

    return min_item


if __name__ == '__main__':
    print lifeskills(20.04, {'ketchup': 2.99, 'avocados': 0.99, 'milk': 3.25})
