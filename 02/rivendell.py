from ib111 import week_02  # noqa


# Consider 11-base with values ⟦0, 1, 2, 3, 4, 5, 6, 7, 8, 9⟧ and ⟦δ⟧ representing <-1>
# ‹elf_digit_sum(num)› returns sum of digit values in 11-base with new special digit ⟦δ⟧

# Example:
#  • digit sum ⟦1729 = (1332)ₑ⟧ je ⟦1 + 3 + 3 + 2 = 9⟧,
#  • or ⟦1234 = (1δ22)ₑ⟧ has sum ⟦1 - 1 + 2 + 2 = 4⟧,
#  • and ⟦999987 = (62334δ)ₑ⟧ has sum ⟦6 + 2 + 3 + 3 + 4 - 1 = 17⟧.

def elf_digit_sum(num):
    value = to_elevenary(num)
    sumValue = 0
    while value > 0:
        if (value % 10) == 0:
            sumValue -= 1
        else:
            sumValue += value % 10
        value //= 10
    return sumValue

def to_elevenary(number):
    value = 0
    power = 1
    while number > 0:
        value += number % 11 * power
        number //= 11
        power *= 10

    return value

def main() -> None: # run tests
    assert elf_digit_sum(10) == 0
    assert elf_digit_sum(1729) == 9
    assert elf_digit_sum(1234) == 4
    assert elf_digit_sum(999987) == 17
    assert elf_digit_sum(305997) == -3


if __name__ == '__main__':
    main()
