'''Write a function that takes two strings, and returns the number of times the
first string appears in the second, without using any of your language's string
processing facilities (i.e., treat the strings as lists of characters).

E.g.
matches('baba', 'abababa') => 2
'''


def matches(x, y):
    count = 0
    len_x = len(x)

    for i in range(0, len(y) - len_x + 1):
        if y[i:i+len_x] == x:
            count += 1

    return count


if __name__ == '__main__':
    print matches('baba', 'abababa')
