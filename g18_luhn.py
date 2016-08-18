'''Implement the Luhn algorithm for validating credit card numbers. (It's too
fiddly to explain on the board, wikipedia has a good explanation).
'''


def luhn(number):
    chars = str(number)
    check_digit = int(chars[-1])
    digits = []

    for i, char in enumerate(reversed(chars[:-1])):
        digit = int(char)

        if not i % 2:
            digit *= 2
            if digit > 9:
                digit -= 9

        digits.append(digit)

    sum_with_check = sum(digits) + check_digit

    return (sum_with_check % 10) == 0


if __name__ == '__main__':
    print luhn('79927398710')
    print luhn('79927398711')
    print luhn('79927398712')
    print luhn('79927398713')  # Should be True
