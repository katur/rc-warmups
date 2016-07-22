'''Write a function that takes a string and prints out the 1st character, then
the 1st 2 characters, etc. until the whole string has been printed.
'''


def marquee(s):
    for i in range(len(s)):
        print s[0:i+1]


if __name__ == '__main__':
    marquee('hi!<3')
