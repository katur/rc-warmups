'''Write a function that takes a filename and a number n, and prints out the
file contents reversed in chunks of n characters.

E.g.
foo.txt contains:
    hello world
    how's it going?

reverser("foo.txt", 3) ->
    ng?goiit 's howld
    worlo hel

Above solution assumes foo.txt does not end in a newline
'''


def reverser(filename, n):
    with open(filename, 'r') as f:
        contents = f.read()

    FIRST_INDEX = len(contents) - n

    res = ''.join([contents[i:i+n] for i in range(FIRST_INDEX, 0, -n)])

    # Tack on the initial chunk, if missed for being less than n characters
    res += contents[0:i]

    print res


if __name__ == '__main__':
    reverser('h18_foo.txt', 4)
