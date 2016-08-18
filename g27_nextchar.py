'''Write a function that takes a string, and collects all pairs of characters
in the string; each pair should have a list of all characters that appear
immediately after it in the string (without duplicates). Use 0 or another
marker for the end of the string.

E.g. next_char("an apple and a banana") ->
{
    'an': [' ', 'd', 'a'],
    'pp': ['l'],
    ' a': ['p', 'n', ' '],
    'na': ['n', 0],
    ...
}
'''


def next_char(string):
    d = {}
    for i in range(len(string) - 1):
        chars = string[i:i+2]

        try:
            following = string[i+2]
        except IndexError:
            following = 0

        # Use a set to avoid duplicates
        if chars in d:
            d[chars].add(following)
        else:
            d[chars] = {following}

    return {k: list(v) for k, v in d.iteritems()}


if __name__ == '__main__':
    print next_char('an apple and a banana')
