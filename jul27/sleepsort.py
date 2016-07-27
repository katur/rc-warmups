'''Write a function that takes a list of numbers, and prints each number n
after an n-second delay.

E.g.
sleepsort([3,1,4]) ->
(one second pause)
1
(two second pause)
3
(three second pause)
4
'''

import time


def sleepsort(l):
    for i, num in enumerate(sorted(l)):
        time.sleep(i + 1)
        print num


if __name__ == '__main__':
    sleepsort([3, 1, 4])
    sleepsort([3, 1, 4, 6, 28, 5, 0])
