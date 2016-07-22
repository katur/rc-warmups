'''Given a string and a list of words, return the word from the list that
appears most often in the string, along with the number of times it appears.
Ignore case but don't do any other NLP-style transformations (stemming etc.).

E.g. winner(['a', 'the', 'cat'], 'The Cat in the Hat') -> ('the', 2)
'''


def winner(words, string):
    # Transform to a set for efficiency
    words = set(words)

    # Record word freqencies
    frequencies = {}
    for word in string.lower().split():
        if word not in words:
            continue

        if word not in frequencies:
            frequencies[word] = 1
        else:
            frequencies[word] += 1

    # Find the max
    maximum = (None, None)
    for word, frequency in frequencies.iteritems():
        if not maximum[1] or frequency > maximum[1]:
            maximum = (word, frequency)

    return maximum


if __name__ == '__main__':
    print winner(['a', 'the', 'cat'], 'The Cat in the Hat')
