from ib111 import week_04  # noqa

# Convert numeric codes to barcodes, use the functions for
# working with barcodes defined in the previous example.
from barcode import \
    barcode_valid, barcode_decode, barcode_encode, barcode_digits, \
    digit_count, digit_slice


def digit_compose(left: int, right: int, base: int,
                  r_size: int) -> int:
    assert digit_count(right, base) <= r_size
    return left * (base ** r_size) + right


def decimal_count(num: int) -> int:
    return digit_count(num, 10)


def decimal_slice(num: int, low: int, digits: int) -> int:
    return digit_slice(num, 10, low, digits)


def bit_compose(left: int, right: int, r_bits: int) -> int:
    return digit_compose(left, right, 2, r_bits)


def decimal_compose(left: int, right: int, r_digits: int) -> int:
    return digit_compose(left, right, 10, r_digits)


# predicate that will decide if it is a valid EAN:
# the last digit is a check digit. EAN exists in several lengths, but
# the algorithm for checking them is always the same, so it is in the parameter

def ean_valid(ean: int, length: int) -> bool:
    checksum = 0
    odd = True
    digits = 0

    while ean > 0:
        digits += 1
        checksum += ean % 10 * ean_digit_weight(odd)
        odd = not odd
        ean //= 10

    return digits <= length and checksum % 10 == 0

# Auxiliary function that describes the weights of individual digits in an EAN
# code (for the purposes of calculating the check digit).

def ean_digit_weight(odd: bool) -> int:
    return 1 if odd else 3

# Creating a valid EAN-13 code from individual components: GS1 prefix (simplified
# corresponds to the country of the manufacturer), manufacturer code (which is at least
# five digits long) and product code itself. The total length of the code without
# checksum must be 12 digits.

def generate_ean(gs1: int, manufacturer: int, product: int,
                 product_digits: int) -> int:
    assert 0 <= gs1 < 1000
    assert manufacturer >= 0
    assert decimal_count(product) <= product_digits
    assert decimal_count(manufacturer) + product_digits <= 10
    manufacturer_digits = 12 - product_digits - 3

    odd = False
    check = 0

    for part in [product, manufacturer, gs1]:
        while part > 0:
            check += part % 10 * ean_digit_weight(odd)
            part //= 10
            odd = not odd

    check = 10 - check % 10

    ean = decimal_compose(gs1, manufacturer, manufacturer_digits)
    ean = decimal_compose(ean, product, product_digits)
    ean = decimal_compose(ean, check, 1)

    assert ean_valid(ean, 13)
    return ean

# The following are two functions for converting between numeric and barcode.
# The first one takes a valid EAN-8 numeric representation as input

def ean8_to_barcode(ean: int) -> int:
    assert ean_valid(ean, 8)
    left = barcode_encode(decimal_slice(ean, 4, 4), 'L')
    right = barcode_encode(decimal_slice(ean, 0, 4), 'R')

    barcode = 0
    barcode = bit_compose(barcode, 0b101, 3)
    barcode = bit_compose(barcode, left, 7 * 4)
    barcode = bit_compose(barcode, 0b01010, 5)
    barcode = bit_compose(barcode, right, 7 * 4)
    barcode = bit_compose(barcode, 0b101, 3)

    assert barcode_valid(barcode, 8, 'L', 'R')
    return barcode

# The last function in this file is used for the reverse conversion:
# creates a numeric representation from the barcode. The input condition
# is that the barcode is valid and encodes 8 digits

def barcode_to_ean8(barcode: int) -> int | None:
    assert barcode_valid(barcode, 8, 'L', 'R')
    left, right = barcode_digits(barcode)
    ean = decimal_compose(barcode_decode(left, 'L'),
                          barcode_decode(right, 'R'), 4)
    if not ean_valid(ean, 8):
        return None
    return ean


def main() -> None:  # demo
    week_04

    assert ean_valid(12345670, 8)
    assert ean_valid(1122334455666, 13)
    assert not ean_valid(12345674, 8)
    assert not ean_valid(1122334455664, 13)
    assert generate_ean(123, 123212, 123, 3) == 1231232121235
    assert generate_ean(444, 12345, 1111, 4) == 4441234511119
    assert ean8_to_barcode(12345670) == 0x5324dea354ea11395
    assert ean8_to_barcode(11112228) == 0x53264c9956cd9b245
    assert barcode_to_ean8(0x5324dea354ea11395) == 12345670
    assert barcode_to_ean8(0x53264c9956cd9b245) == 11112228
    assert barcode_to_ean8(0x53264c9956cd9b395) is None


if __name__ == '__main__':
    main()
