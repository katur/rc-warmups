'''Write a function that takes two lists: L1 contains arbitrary data, L2
contains pairs of numbers. For each pair in L2, swap the corresponding elements
in L1, and return the result at the end.

E.g.
swap(['a', 'b', 'c'], [(0, 2), (1, 2)]) -> ['c', 'a', 'b']
'''


def swap(l1, l2):
    res = list(l1)  # Copy to not mess with original list l1

    for pair in l2:
        swap_positions(res, *pair)

    return res


def swap_positions(l, i1, i2):
    """Swap the elements at indices i1 and i2 in list l."""
    temp = l[i1]
    l[i1] = l[i2]
    l[i2] = temp


if __name__ == '__main__':
    print swap(['a', 'b', 'c'], [(0, 2), (1, 2)])
