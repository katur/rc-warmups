'''Write a function that takes an array of numbers and returns the largest sum
of 3 adjacent numbers in the array.

E.g. maxrun([-4, 4, 8, -2, 7, -13]) -> 13
'''


def max_run(l):
    largest = None

    for i in range(0, len(l) - 2):
        x = sum(l[i:i+3])
        if largest is None or x > largest:
            largest = x

    return largest


if __name__ == '__main__':
    print max_run([-4, 4, 8, -2, 7, -13])
