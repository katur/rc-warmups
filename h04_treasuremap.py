'''Given a hash/dict/map/pairlist that contains rooms with a list of their
neighbours, write a function that takes a start room and an end room, and
returns a path between them.

E.g.
rooms = {'kit': ['lib', 'bath'],
         'bath': ['kit', 'foyer'],
         'foyer': ['bath', 'din']}

treasure_map('foyer', 'lib')
-> ['foyer', 'bath', 'kit', 'lib']
'''

ROOMS = {
    'kit': ['lib', 'bath'],
    'bath': ['kit', 'foyer'],
    'foyer': ['bath', 'din'],
}


def search_outgoing(path, goal):
    current = path[-1]

    # Solution found
    if current == goal:
        return path

    for room in ROOMS[current]:
        # Skip cycles
        if room in path:
            continue

        solution = search_outgoing(path + [room], goal)
        if solution:
            return solution


def treasure_map(start, end):
    return search_outgoing([start], end)


if __name__ == '__main__':
    print treasure_map('foyer', 'lib')
