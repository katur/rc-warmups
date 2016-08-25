'''Write a function that takes a list of sorted lists of numbers, and returns a
single sorted list with all of the numbers. Don't use your language's sort
function.

E.g.
merge([[1, 5, 7], [3, 4, 9]]) -> [1, 3, 4, 5, 7, 9]
'''


def merge(lists):
    return merge_recursive(lists, [])


def merge_recursive(lists, res):
    # Remove empty sublists
    lists = [l for l in lists if l]

    if not lists:
        return res

    min_num = None
    min_index = None

    for i, l in enumerate(lists):
        num = l[0]
        if not min_num or num < min_num:
            min_num = num
            min_index = i

    res.append(lists[min_index].pop(0))
    return merge_recursive(lists, res)


if __name__ == '__main__':
    print merge([[1, 5, 7], [3, 4, 9]])
