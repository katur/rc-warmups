'''Recursively flatten an arbitrarily nested list of lists.

E.g. [[1, 2, 3], [4, [5]]] -> [1, 2, 3, 4, 5]
'''


def flatten(l):
    output = []
    for element in l:
        extract(element, output)
    return output


def extract(element, output):
    if isinstance(element, list):
        [extract(el, output) for el in element]
    else:
        output.append(element)


if __name__ == '__main__':
    print flatten([[1, 2, 3], [4, [5]]])
