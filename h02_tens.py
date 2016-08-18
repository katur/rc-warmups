'''Write a function that takes a list of numbers and returns all adjacent
sublists that sum to 10. You can assume that all numbers are non-negative.

E.g.
tens([2, 3, 5, 5, 4, 1, 0, 9, 1])
-> [ [2,3,5], [5,5], [5,4,1], [5,4,1,0], [1,0,9], [0,9,1], [9,1]]
'''

TEN = 10


def tens(all_numbers):
    start = 0
    end = 1

    while start < len(all_numbers):
        numbers = all_numbers[start:end]
        sum_numbers = sum(numbers)

        if sum_numbers == TEN:
            yield numbers

        if sum_numbers >= TEN or end > len(all_numbers):
            start += 1
            end = start + 1
        else:
            end += 1


if __name__ == '__main__':
    print list(tens([2, 3, 5, 5, 4, 1, 0, 9, 1]))
