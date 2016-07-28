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

SQUARE = 'square'
DIAMOND = 'diamond'


def art_write(s, number):
    out = ''

    # Subtract 1 from number so that the middle is 0-indexed
    middle = (number - 1) / 2.0

    for row in range(number):
        for column in range(number):
            if s == SQUARE:
                out += process_square_spot()
            elif s == DIAMOND:
                out += process_diamond_spot(row, column, middle)
        out += '\n'

    print out


def process_square_spot():
    return 'x '


def process_diamond_spot(row, column, middle):
    distance_from_middle_row = abs(row - middle)
    distance_from_middle_column = abs(column - middle)
    summed_distance = distance_from_middle_row + distance_from_middle_column

    # I'm not totally sure why I have to add 0.5... something about wanting to
    # round up in the odd cases
    if summed_distance <= (middle + 0.5):
        return 'x '
    else:
        return '  '


if __name__ == '__main__':
    art_write(SQUARE, 3)
    art_write(SQUARE, 8)
    art_write(SQUARE, 15)
    art_write(DIAMOND, 3)
    art_write(DIAMOND, 4)
    art_write(DIAMOND, 5)
    art_write(DIAMOND, 6)
    art_write(DIAMOND, 7)
    art_write(DIAMOND, 8)
    art_write(DIAMOND, 9)
