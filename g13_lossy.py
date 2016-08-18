'''Write a function that takes a filename, reads the file, and
prints out the contents *without* any vowels.

E.g. lossy("taleoftwocities.txt") -> twsthbstftms,tws...

By Emily and Katherine
'''

VOWELS = 'AEIOUaeiou'


def lossy(filename):
    with open(filename, 'r') as f:
        for line in f:
            print ''.join([char for char in line[:-1] if char not in VOWELS])


if __name__ == '__main__':
    lossy('g13_taleoftwocities.txt')
