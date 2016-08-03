'''Write a function that takes a starting number of bunnies and a litter size,
and prints out the number of bunnies in the first 20 generations. Remember that
bunnies reproduce asexually and are immortal.

E.g.
bunnies(5, 3)
5   # baby bunnies
5   # adolescent bunnies
20  # 5 adults + 15 babies
35  # 5 adults + 15 adolescents + 15 babies
95  # etc.
'''


def bunnies(starting, litter_size):
    babies = starting
    adolescents = 0
    adults = 0
    print babies + adolescents + adults

    for i in range(20):
        adults += adolescents
        adolescents = babies
        babies = adults * litter_size
        print babies + adolescents + adults


if __name__ == '__main__':
    bunnies(5, 3)
