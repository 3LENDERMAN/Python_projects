from ib111 import week_04  # noqa

# Encoding of bar codes (black and white stripes)
# Example:
#    ┌┄┬┄┬┄┬┄┬┄┬┄┬┄┐
#    ┆ ┆ ┆█┆ ┆ ┆█┆█┆
#    ┆ ┆ ┆█┆ ┆ ┆█┆█┆
#    ┆ ┆ ┆█┆ ┆ ┆█┆█┆
#    ┆ ┆ ┆█┆ ┆ ┆█┆█┆
#    ┆ ┆ ┆█┆ ┆ ┆█┆█┆
#    └┄┴┄┴┄┴┄┴┄┴┄┴┄┘
#     0 0 1 0 0 1 1

# Every digit has one of the three encodings: ‹L›, ‹R› and (‹G›)
# Example mentioned is encoded in ‹L› and below is in inverted, so ‹R›

#    ┌┄┬┄┬┄┬┄┬┄┬┄┬┄┐
#    │█┆█┆ ┆█┆█┆ ┆ │
#    │█┆█┆ ┆█┆█┆ ┆ │
#    │█┆█┆ ┆█┆█┆ ┆ │
#    │█┆█┆ ┆█┆█┆ ┆ │
#    │█┆█┆ ┆█┆█┆ ┆ │
#    └┄┴┄┴┄┴┄┴┄┴┄┴┄┘
#     1 1 0 1 1 0 0

# EAN bar codes have 5 bars:
#  • beginning group 101,
#  • first half of digits, seven bars,
#  • middle group 01010,
#  • second half of digits, seven bars,
#  • end group 101.

# Example of two digits (2 a 2)
# first encoded ‹L›, second ‹R›
# 0 and 1 as _ and X
#   ┌┄┬┄┬┄┬┄┬┄┬┄┬┄┬┄┬┄┬┄┬┄┬┄┬┄┬┄┬┄┬┄┬┄┬┄┬┄┬┄┬┄┬┄┬┄┬┄┬┄┐
#   ┆▓┆ ┆▓┆ ┆ ┆█┆ ┆ ┆█┆█┆ ┆▓┆ ┆▓┆ ┆█┆█┆ ┆█┆█┆ ┆ ┆▓┆ ┆▓┆
#   ┆▓┆ ┆▓┆ ┆ ┆█┆ ┆ ┆█┆█┆ ┆▓┆ ┆▓┆ ┆█┆█┆ ┆█┆█┆ ┆ ┆▓┆ ┆▓┆
#   ┆▓┆ ┆▓┆ ┆ ┆█┆ ┆ ┆█┆█┆ ┆▓┆ ┆▓┆ ┆█┆█┆ ┆█┆█┆ ┆ ┆▓┆ ┆▓┆
#   ┆▓┆ ┆▓┆ ┆ ┆█┆ ┆ ┆█┆█┆ ┆▓┆ ┆▓┆ ┆█┆█┆ ┆█┆█┆ ┆ ┆▓┆ ┆▓┆
#   ┆▓┆ ┆▓┆ ┆ ┆█┆ ┆ ┆█┆█┆ ┆▓┆ ┆▓┆ ┆█┆█┆ ┆█┆█┆ ┆ ┆▓┆ ┆▓┆
#   └┄┴┄┴┄┴┄┴┄┴┄┴┄┴┄┴┄┴┄┴┄┴┄┴┄┴┄┴┄┴┄┴┄┴┄┴┄┴┄┴┄┴┄┴┄┴┄┴┄┘
#    X _ X 0 0 1 0 0 1 1 _ X _ X _ 1 1 0 1 1 0 0 X _ X

def digit_count(num: int, base: int) -> int:
    result = 0
    while num > 0:
        num //= base
        result += 1
    return result

def digit_slice(num: int, base: int, low: int, size: int) -> int:
    return num // base ** low % base ** size

def bit_count(num: int) -> int:
    return digit_count(num, 2)

def bit_slice(num: int, low: int, size: int) -> int:
    return digit_slice(num, 2, low, size)

# Predicate ‹barcode_valid›, checks validity of the bar code. 
# Parameters ‹digit_count› (number of digits), ‹l_coding› (encoding from left side)
# (‹L› or ‹R›) and ‹r_coding› from right side.

def barcode_valid(barcode: int, digit_count: int,
                  l_coding: str, r_coding: str) -> bool:

    assert l_coding == 'L' or l_coding == 'R'
    assert r_coding == 'L' or r_coding == 'R'
    assert digit_count % 2 == 0

    # set useful constants
    boundary_size = 3
    center_size = 5
    total_marker_size = 2 * boundary_size + center_size

    if bit_count(barcode) < total_marker_size:
        return False  # not enough space for all required markers
    if (bit_count(barcode) - total_marker_size) % 2 != 0:
        return False  # does not evenly split into halves

    half_width = barcode_half_width(barcode)
    center_start = boundary_size + half_width
    center_end = center_start + center_size

    if bit_slice(barcode, 0, boundary_size) != 0b101:
        return False  # bad start marker
    if bit_slice(barcode, center_end + half_width, 3) != 0b101:
        return False  # bad end marker
    if bit_slice(barcode, center_start, center_size) != 0b01010:
        return False

    # Check if numbers are correctly encoded:
    if half_width % 7 != 0:
        return False
    if 2 * half_width // 7 != digit_count:
        return False

    left, right = barcode_digits(barcode)

    if not barcode_valid_digits(left, l_coding):
        return False
    if not barcode_valid_digits(right, r_coding):
        return False

    return True

def barcode_half_width(barcode: int) -> int:
    bits = bit_count(barcode)
    assert bits >= 11
    assert (bits - 11) % 2 == 0
    return (bits - 11) // 2

def barcode_digits(barcode: int) -> tuple[int, int]:
    half_width = barcode_half_width(barcode)
    left = bit_slice(barcode, 8 + half_width, half_width)
    right = bit_slice(barcode, 3, half_width)
    return (left, right)

def barcode_encode_digit(digit: int, coding: str) -> int:
    assert 0 <= digit <= 9
    assert coding == 'L' or coding == 'R'

    codes = [0b0001101, 0b0011001, 0b0010011, 0b0111101, 0b0100011,
             0b0110001, 0b0101111, 0b0111011, 0b0110111, 0b0001011]

    code = 0
    shift = 1
    bits = codes[digit]

    for _ in range(7):
        area = bits % 2
        bits //= 2
        if coding == 'L':
            code += area * shift
        if coding == 'R':
            code += (1 - area) * shift
        shift *= 2

    return code


# Decode digits, if function will not succeed, return None:
def barcode_decode_digit(code: int, coding: str) -> int | None:
    assert code >= 0
    for digit in range(10):
        if barcode_encode_digit(digit, coding) == code:
            return digit
    return None

def barcode_valid_digits(areas: int, coding: str) -> bool:
    base = 2 ** 7
    while areas > 0:
        if barcode_decode_digit(areas % base, coding) is None:
            return False
        areas //= base
    return True

def barcode_decode(areas: int, coding: str) -> int:
    assert barcode_valid_digits(areas, coding)
    result = 0
    base = 2 ** 7
    shift = 1

    while areas > 0:
        digit = barcode_decode_digit(areas % base, coding)
        areas //= base
        # decode each digit
        assert digit is not None
        result += digit * shift
        shift *= 10
    return result


# Create valid numerical area of bar code (positive number)

def barcode_encode(digits: int, coding: str) -> int:
    assert digits >= 0
    result = 0
    base = 2 ** 7
    shift = 1
    while digits > 0:
        result += barcode_encode_digit(digits % 10, coding) * shift
        shift *= base
        digits //= 10
    assert barcode_valid_digits(result, coding)
    return result


def main() -> None:  # tests
    assert not barcode_valid(0b111, 0, 'L', 'L')
    assert barcode_valid(0b10101010101, 0, 'L', 'L')
    code_27_ok = 0b101_0010011_01010_0111011_101
    code_27_bad1 = 0b101_0010011_01010_0101011_101
    code_27_bad2 = 0b101_0010111_01010_0111011_101
    code_1337_ok = 0b101_0011001_0111101_01010_1000010_1000100_101
    assert barcode_valid(code_27_ok, 2, 'L', 'L')
    assert barcode_valid(code_1337_ok, 4, 'L', 'R')
    assert not barcode_valid(code_27_bad1, 2, 'L', 'L')
    assert not barcode_valid(code_27_bad2, 2, 'L', 'L')
    code_27_l, code_27_r = barcode_digits(code_27_ok)
    assert code_27_l == 0b0010011
    assert code_27_r == 0b0111011
    assert barcode_decode(code_27_l, 'L') == 2
    assert barcode_decode(code_27_r, 'L') == 7
    assert barcode_encode(13, 'L') == 0b00110010111101
    assert barcode_encode(37, 'R') == 0b10000101000100


if __name__ == '__main__':
    week_04
    main()
