'''Write a function that takes an array of 5 numbers, and returns a string
representing their value as a poker hand.
'''

from collections import OrderedDict


def poker(hand):
    hand = sorted(hand)

    # Create dictionary of quantity of each card
    organized_hand = OrderedDict()
    for card in hand:
        if card not in organized_hand:
            organized_hand[card] = 1
        else:
            organized_hand[card] += 1

    # Check for Straight or Nothing
    if len(organized_hand) == 5:
        for i in range(len(hand))[1:]:
            if hand[i] != (hand[i-1] + 1):
                return 'Nothing'
        return 'Straight'

    # Create set of quantities
    sizes = set(organized_hand.values())

    # Check for Full House or x-in-a-row
    if sizes == set([2, 3]):
        return 'Full House'
    else:
        return '{} in a row'.format(max(sizes))


if __name__ == '__main__':
    print poker([1, 2, 1, 2, 2])
    print poker([3, 2, 5, 4, 1])
    print poker([3, 3, 3, 4, 1])
    print poker([4, 1, 5, 2, 5])
    print poker([1, 2, 3, 4, 9])
