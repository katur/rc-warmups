'''Write a function that takes a list of coins and a goal, and returns a
list of the coins that add up to the goal, or False if it's not possible.

E.g. change([1,1,5,5,10], 11) -> [1,5,5] (or [1,10])
     change([1,5,10,25], 9) -> False
'''


def change(coins, goal):
    return recurse(coins, 0, [], goal)


def recurse(coins, index, accrued, goal):
    """
    coins: original list of coins
    index: candidate coin we're testing
    accrued: coins added to answer so far
    goal: the target sum
    """
    # Base case for success
    if sum(accrued) == goal:
        return accrued

    # Base cases for failure
    if index >= len(coins):
        return False

    if sum(accrued) > goal:
        return False

    candidate = coins[index]

    with_candidate = recurse(coins, index + 1, accrued + [candidate], goal)

    if with_candidate:
        return with_candidate

    return recurse(coins, index + 1, accrued, goal)


if __name__ == '__main__':
    print change([1, 1, 5, 5, 10], 11)
    print change([1, 1, 5, 5, 10], 22)
    print change([1, 1, 5, 5, 10], 21)
    print change([1, 5, 10, 25], 9)
