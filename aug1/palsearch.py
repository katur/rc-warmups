'''Write a function that takes a string and a filename, and finds a palindrome
containing the substring in the file. Ignore case and all non-letter characters
when searching for the palindrome, but return the actual text.

Update: no need to return the actual text.

E.g.
$ cat test.txt
Madam, I'm too hot to hoot.

palsearch('o', 'test.txt')
-> 'o'
-> 'oo'
-> 'o hot to ho'
(any of these is fine)
'''


def get_string_from_file(filename):
    with open(filename, 'r') as f:
        return f.read()


def is_palindrome(s):
    """Check if s is a palindrome in linear time."""
    return s == s[::-1]


def find_all_occurrences(string, substring):
    """Find all instances of substring in string in linear time.

    Returns the starting index of each occurrence.
    """
    start = 0

    while True:
        start = string.find(substring, start)  # Begin the search at start
        if start == -1:
            return
        yield start
        start += 1


def palsearch(substring, filename):
    string = get_string_from_file(filename)
    charseq = ''.join(char for char in string if char.isalpha())
    for_spots = find_all_occurrences(charseq, substring)
    rev_spots = find_all_occurrences(charseq, substring[::-1])

    for for_start in for_spots:
        for_end = for_start + len(substring)

        for rev_start in rev_spots:
            rev_end = rev_start + len(substring)

            if for_start <= rev_start:
                substring = charseq[for_start:rev_end]
                if is_palindrome(substring):
                    return substring
            else:
                substring = charseq[rev_start:for_end]
                if is_palindrome(substring):
                    return substring


##########################################################################
# This is a bad solution which starts by finding all the palindromes in s,
# not initially reducing the search space to occurrences of the substring.
##########################################################################

def find_all_palindromes(s):
    """Find all palindromes in s in O(n^3) time.

    Could be improved to O(n^2) by finding for each char in s all the
    palindromes with char as the middle.
    """
    palindromes = set()

    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)

    return palindromes


def palsearch_slow(substring, filename):
    string = get_string_from_file(filename)
    charseq = ''.join(char for char in string if char.isalpha())
    all_palindromes = find_all_palindromes(charseq)
    palindromes_with_substring = set()

    for palindrome in all_palindromes:
        if substring in palindrome:
            palindromes_with_substring.add(palindrome)

    return palindromes_with_substring


if __name__ == '__main__':
    print palsearch('o', 'test.txt')
    print palsearch('hot', 'test.txt')
    print palsearch_slow('o', 'test.txt')
