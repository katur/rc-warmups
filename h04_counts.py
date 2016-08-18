'''Given a list of numbers, print out all numbers n that appear between n and
2n (inclusive) in the list.

counts([3, 0, 1, 4, 3, 3, 4, 1])
1
3
(0 appears too often, 4 not enough often)
'''


def counts(l):
    frequencies = {}
    for num in l:
        if num in frequencies:
            frequencies[num] += 1
        else:
            frequencies[num] = 1

    for num, frequency in frequencies.iteritems():
        if frequency >= num and frequency <= (2 * num):
            print num


if __name__ == '__main__':
    counts([3, 0, 1, 4, 3, 3, 4, 1])
