'''Given a list of 3 numbers (seconds in a minute, minutes in an hour, hours
in a day) and 2 strings representing times (in HH:MM:SS format), calculate the
number of seconds between the two times.

E.g. [20, 60, 24], '01:05:15', '01:06:05' -> 10
'''

import operator


def convert(string):
    h, m, s = string.split(':')
    return [int(s), int(m), int(h)]


def get_max_then_min(a, b):
    if [i for i in reversed(a)] > [i for i in reversed(b)]:
        return (a, b)
    else:
        return (b, a)


def astroclock(spec, a, b):
    max_, min_ = get_max_then_min(convert(a), convert(b))
    difference = list(map(operator.sub, max_, min_))

    for i in range(len(difference)):
        if difference[i] < 0:
            difference[i+1] -= 1
            difference[i] += spec[i]

    return (difference[0] +
            difference[1] * spec[0] +
            difference[2] * spec[1])


if __name__ == '__main__':
    print astroclock([20, 60, 24], '01:05:15', '01:06:05')
    print astroclock([60, 60, 24], '03:45:36', '02:50:36')
