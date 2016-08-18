'''Write a function that takes a number n and a list of numbers and prints out
list elements until every number up to and including n has been printed at
least once, then prints "BINGO". don't print the rest of the list. if all the
numbers don't appear, print the whole list, *no* "BINGO".
'''


def bingo(n, l):
    seen = set()

    for item in l:
        print item
        if item <= n:
            seen.add(item)

        if len(seen) >= n:
            print "BINGO"
            return


if __name__ == '__main__':
    bingo(4, [1, 5, 6, 3, 4, 8, 4, 5, 4, 4, 2, 7, 7, 7, 11, 11, 7, 11])
