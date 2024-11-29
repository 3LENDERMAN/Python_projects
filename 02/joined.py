from ib111 import week_02  # noqa

# ‹count› creates number by chaining numbers together starting from ‹start›
# Numbers will be chained in binary. Example:
# ‹joined(1, 3)› will chain sequence ⟦(1)₂ = 1⟧, ⟦(10)₂ = 2⟧, ⟦(11)₂ = 3⟧
# and returns ⟦(11011)₂ = 27⟧.

def joined(start,count):
    total_length = 0
    length = 0
    final_sum = 0
    for i in range(start + count - 1, start - 1, -1):
        curr_number = to_binary(i)
        length = get_length(curr_number)
        for x in range(1, length + 1):
            val = get_digit(curr_number, x)   
            if val == 1:
                final_sum += 2 ** total_length
            total_length += 1
    return final_sum

def get_digit(number, index):
    digit = 0
    while index > 0:
        digit = number % 2
        number //= 10
        index -= 1
    return digit

def get_length(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count

def to_binary(number):
    if number == 0:
        return 0
    value = 0
    power = 1
    while number > 0:
        value += number % 2 * power
        number //= 2
        power *= 10

    return value

def main() -> None: # run tests
    assert joined(1, 3) == 0b11011
    assert joined(10, 4) == 0b1010101111001101
    assert joined(8, 5) == 0b10001001101010111100
    assert joined(99, 2) == 0b11000111100100
    assert joined(999, 3) == 0b111110011111111010001111101001
    assert joined(1111, 1) == 0b10001010111


if __name__ == "__main__":
    main()
