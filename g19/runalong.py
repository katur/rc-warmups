'''Given a string with many repeated characters, output a compressed string
by replacing each run of characters with the character and the length of the
run.

E.g. 'aaabccccaa' -> 'a3bc4a2'
'''


def run_along(string):
    output = []

    def append_to_output(char, count):
        output.append(char)

        if count > 1:
            output.append(str(count))

    previous = string[0]
    count = 1

    for current in string[1:]:
        if previous == current:
            count += 1
        else:
            append_to_output(previous, count)
            previous = current
            count = 1

    append_to_output(previous, count)
    return ''.join(output)


def run_along2(string):
    def run_single_char(index):
        """Iterate from this index to the first mismatch.
        Return (char at index, end of run index (exclusive))
        """
        char = string[index]

        index += 1
        while index < len(string) and string[index] == char:
            index += 1

        return (char, index)

    output = ''
    start = 0
    end = None

    while end < len(string):
        (char, end) = run_single_char(start)
        length = end - start

        output += char
        if length > 1:
            output += str(length)

        start = end

    return output


if __name__ == '__main__':
    print run_along('aaabccccaa')
    print run_along2('aaabccccaa')
