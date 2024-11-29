from ib111 import week_03  # noqa

# tuple ‹(base, digits)›: ‹digits› list of ciphers in such base, 
# type of int in interval [0, ‹base› - 1]. Index of list ‹digits› corresponds to base powers:
#  • ‹(10, [2, 9])› in decimal ‹2 * 1 + 9 * 10 = 92›
#  • ‹(7, [2, 1])› in seven-base ‹2 * 1 + 1 * 7 = 9›

# Converts ‹number› to base representation in ‹base›:
def to_digits(number, base):
    number_list = []
    while number > 0:
        number_list.append(number % base)
        number //= base
    return (base, number_list)

# From cipher representation ‹number› creates ‹int› value:
def from_digits(number):
    base, digits = number
    power = 1
    value = 0
    for digit in digits:
        value += power * digit
        power *= base
    return value

# ‹convert_digits› converts number to different base representation:
def convert_digits(number, base):
    return to_digits(from_digits(number), base)


def main(): # run tests
    assert to_digits(92, 10) == (10, [2, 9])
    assert to_digits(9, 7) == (7, [2, 1])
    assert to_digits(33, 16) == (16, [1, 2])
    assert to_digits(10, 2) == (2, [0, 1, 0, 1])
    assert convert_digits((16, [1, 2]), 10) == (10, [3, 3])
    assert to_digits(33, 7) == (7, [5, 4])
    assert from_digits((7, [5, 4])) == 33
    assert from_digits((3, [1, 0, 1])) == 10
    assert from_digits(to_digits(1382, 24)) == 1382
    assert to_digits(0, 10) == (10, [])

    for base in range(2, 12):
        for n in range(2, 200):
            assert from_digits(to_digits(n, base)) == n


if __name__ == "__main__":
    main()
