'''Write a function that takes a filename and a character, and prints the lines
in the file, ordered by the number of times the character appears in each line.

E.g.
rank('foo.txt', 'e') ->
    how's everyone doing?
    hey,
    hello world!

foo.txt
    hey,
    hello world!
    how's everyone doing?
'''

import re


def rank(filename, char):
    count_to_lines = {}

    with open(filename, 'r') as f:
        for line in f:
            count = get_count(char, line)

            if count not in count_to_lines:
                count_to_lines[count] = [line]
            else:
                count_to_lines[count].append(line)

    for count, lines in sorted(count_to_lines.items(), reverse=True):
        for line in lines:
            # Since print adds a newline, remove the newline already there
            print line[:-1]


def get_count(char, s):
    """Count number of char in string s."""
    return sum(1 for match in re.finditer(char, s))


if __name__ == '__main__':
    rank('h24_foo.txt', 'e')
