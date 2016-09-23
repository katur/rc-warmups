'''Write a function that models the elevators in a building. It will take 2
arguments:

    - a list of numbers representing the floor each elevator starts on
    - a list of (number, boolean) pairs representing elevator moves (so
      (3, True) would mean to move elevator #3 up one floor; False means down)

Return a list representing the ending position of each elevator.

E.g.
elevators([0, 0, 0], [(0, True), (2, False), (0, True), (1, True), (0, False)]
    => [1, 1, -1]
'''


def elevators(floors, moves):
    for elevator, up in moves:
        if up:
            floors[elevator] += 1
        else:
            floors[elevator] -= 1

    return floors


if __name__ == '__main__':
    print elevators(
        [0, 0, 0], [(0, True), (2, False), (0, True), (1, True), (0, False)])
