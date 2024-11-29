from ib111 import week_02  # noqa

# ‹power_digit_sum›, returns special digit sum of ‹number›
# Each number exponentiate to the value of the index 
# Numbering from left where index of first digit has value 1
# ‹power_digit_sum› calculation will be done in seven-base.

# Example: number ⟦1234⟧ is seven base is: ⟦(3412)₇⟧ – ⟦3⋅7³ + 4⋅7² + 1⋅7¹ + 2⋅7⁰ = 1029 
# + 196 + 7 + 2 = 1234⟧. ‹power_digit_sum(1234)› gets us ⟦3¹ + 4² + 1³ + 2⁴ = 36⟧.

def power_digit_sum(number):
    value = to_seven_base(number)
    sum_val = 0
    length = get_length(value)
    for i in range(1, length + 1):
        digit = get_digit(value, i)
        sum_val += digit ** (length - i + 1)
    return sum_val

# Convert decimal number to seven-base number
def to_seven_base(number):
    if number == 0:
        return 0
    value = 0
    power = 1
    while number > 0:
        value += number % 7 * power
        number //= 7
        power *= 10

    return value

def get_length(number):
    count = 0
    while number > 0:
        number //= 10  # Count digits in decimal numbre
        count += 1
    return count

def get_digit(number, index):
    digit = 0
    for _ in range(1, index + 1):
        digit = number % 10  # Get digit in decimal number
        number //= 10
    return digit

def main() -> None: # run tests
    assert power_digit_sum(7) == 1
    assert power_digit_sum(1234) == 36
    assert power_digit_sum(333) == 95
    assert power_digit_sum(52891) == 46693


if __name__ == "__main__":
    main()
