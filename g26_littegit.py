'''Write a program that, given a directory name, makes a backup
directory called name.bak with copies of everything under the original
directory.

E.g.

foo     - bar
        - baz   -bap
                -bop
        - quux

CREATES:

foo.bak - bar
        - baz   -bap
                -bop
        - quux
'''

from shutil import copytree


def little_git(src):
    dst = src + '.bak'
    copytree(src, dst)


if __name__ == '__main__':
    little_git('g26_foo')
