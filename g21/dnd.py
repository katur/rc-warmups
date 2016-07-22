'''Take a string representing a roll in d&d ('d4+3' means to roll a 4-sided die
and add 3 to the result, '2d6' means roll 2 6-sided dice) and print out 3
random rolls.

E.g. dnd('2d5+1')
-> 7
   4
   9
'''

import math
import random
import re


def roll_die(num_sides):
    return math.ceil(random.random() * num_sides)


def parse_dnd_string(string):
    m = re.match('^(\d*)d(\d+)([\+\-]?)(\d*)$', string)
    return m.groups()


def calculate_dnd_roll(num_dice, num_sides, operation, extra_num):
    if not num_dice:
        num_dice = '1'

    result = 0

    for i in range(int(num_dice)):
        result += roll_die(int(num_sides))

    if operation == '+':
        result += int(extra_num)
    elif operation == '-':
        result -= int(extra_num)

    return result


def dnd(string):
    print string
    parts = parse_dnd_string(string)
    for i in range(3):
        print calculate_dnd_roll(*parts)
    print ''


if __name__ == '__main__':
    dnd('d4+3')
    dnd('2d6')
    dnd('d7')
    dnd('2d5+1')
