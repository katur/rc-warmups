'''Write a function that takes an ascii string, and replaces all adjacent
characters of the same type with the first character of that type.
The 3 types are consonants, vowels, and other (whitespace, punctuation, etc.)

E.g.
lossy("Spring beets - $2/each!") -> "Sin bet ec!")
'''

VOWELS = 'aeiouAEIOU'


def lossy(s):
    res = ''
    for char in s:
        if not res or not same_type(char, res[-1]):
            res += char

    return res


def same_type(a, b):
    for test in (is_other, is_vowel, is_consonant):
        if test(a) and test(b):
            return True

    return False


def is_vowel(char):
    return char in VOWELS


def is_consonant(char):
    return char.isalpha() and char not in VOWELS


def is_other(char):
    return not char.isalpha()


if __name__ == "__main__":
    print lossy("Spring beets - $2/each!")
