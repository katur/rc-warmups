'''Write a command line tool that takes a string and number. The string will be
either 'square' or 'diamond', and the number will be the maximum width of the
desired shape. Draw the shape using the character of your choice.

E.g.
$ art square 3
x x x
x x x
x x x

$ art diamond 3
  x
x x x
  x

$ art diamond 4
  x x
x x x x
x x x x
  x x
'''

import math

SQUARE = 'square'
DIAMOND = 'diamond'


def art_write(s, number):
    out = ''

    for row in range(number):
        for column in range(number):
            if s == SQUARE:
                out += process_square_spot()
            elif s == DIAMOND:
                out += process_diamond_spot(number, row, column)
        out += '\n'

    print out


def process_square_spot():
    return 'x '


def process_diamond_spot(number, row, column):
    middle_index = (number - 1) / 2.0

    distance_from_middle_row = abs(row - middle_index)
    distance_from_middle_column = abs(column - middle_index)
    summed_distance = distance_from_middle_row + distance_from_middle_column

    if summed_distance <= (number / 2.0):
        return 'x '
    else:
        return '  '


if __name__ == '__main__':
    art_write(SQUARE, 3)
    art_write(DIAMOND, 3)
    art_write(DIAMOND, 4)
    art_write(DIAMOND, 5)
    art_write(DIAMOND, 6)
    art_write(DIAMOND, 7)
    art_write(DIAMOND, 8)
    art_write(DIAMOND, 9)
