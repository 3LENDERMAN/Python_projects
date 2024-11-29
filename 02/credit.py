from ib111 import week_02  # noqa

# Predicate checks valid credit card number using Luhn algorithm:
#  1. Double every second value from right side; if value >9 deduct 9
#  2. Sum all numbers from 1. and on odd indexes excluding first from right
#  3. NUmber is valid if sum of all numbers is divisible by 10.

# For 28316 control number is 6 and sum: 
# ⟦2 + (2⋅8 - 9) + 3 + 2⋅1 = 2 + 7 + 3 + 2 = 14⟧.
# After adding control number, sum is 20 which is divisible with 10 
# and number is thus valid.

def is_valid_card(number):
    control = number % 10
    number //= 10
    index = 2
    sumVal = 0
    while number > 0:
        if index % 2 == 0:
            value = number % 10
            if (value * 2) > 9:
                value = (value * 2) - 9
                sumVal += value
            else:
                sumVal += value * 2
        else:
            sumVal += number % 10
        index += 1
        number //= 10
    if (sumVal + control) % 10 == 0:
        return True
    return False

def main():
    assert is_valid_card(28316)
    assert is_valid_card(4556737586899855)
    assert is_valid_card(4929599116478604)
    assert is_valid_card(4929300836739668)
    assert not is_valid_card(4929300835539668)
    assert not is_valid_card(4929300836739328)
    assert not is_valid_card(5101180000000000007)

    assert is_valid_card(5294967072531977)
    assert is_valid_card(5354598557505686)
    assert is_valid_card(2720993849498580)


if __name__ == "__main__":
    main()
