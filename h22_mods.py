'''Write a function that takes a list of numbers, and a number n. Split the
input list into n lists, where all the elements in each list are the same mod
n.

E.g. mods([9, 5, 3, 302], 3) ->
    [
        [9, 3],     # 0 mod 3
        [],         # 1 mod 3 - none
        [5, 302]    # 2 mod 3
    ]
'''


def mods(l, n):
    out = []
    for i in range(n):
        out.append([])

    for item in l:
        mod = item % n
        out[mod].append(item)

    return out


if __name__ == '__main__':
    print mods([9, 5, 3, 302], 3)
