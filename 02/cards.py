from ib111 import week_02  # noqa

# Predicte ‹is_visa›, is True, when parameter number is valid VISA card number
# It starts with 4, and has 13, 16, or 19 numerals and is valid number from <credit> file

def is_visa(number):
    length = get_length(number)
    if number // 10 ** (length - 1) != 4:
        return False
    if length != 13 and length != 16 and length != 19:
        return False
    if not is_valid_card(number):
        return False
    
    return True
    
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

def get_length(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count

# Predicate <is_mastercard> is True, when number is valid Mastercard number
# Thats: starts with 50–55, or 22100–27209, has 16 numerals and is valid credit card number

def is_mastercard(number):
    length = get_length(number)
    if length != 16:
        return False
    value = number // 10 ** (length - 2)
    if value >= 50 and value <= 55:
        return True
    value = number // 10 ** (length - 5)
    if value >= 22100 and value <= 27209:
        return True
    return False

def main(): # run simple tests
    assert is_visa(4111111111111111)
    assert is_visa(4012888888881881)
    assert is_visa(4988438843884305)
    assert is_visa(4646464646464644)
    assert is_visa(4199350000000002)
    assert is_visa(4222222222222)
    assert is_visa(4111111111111111110)

    assert not is_visa(411111111111116)
    assert not is_visa(5500000000000004)
    assert not is_visa(4929300836739328)

    assert is_mastercard(5500000000000004)
    assert is_mastercard(5555555555554444)
    assert is_mastercard(5105105105105100)
    assert is_mastercard(5424000000000015)
    assert is_mastercard(2223520443560010)
    assert is_mastercard(5101180000000007)
    assert is_mastercard(2222400070000005)

    assert not is_mastercard(4012888888881881)
    assert not is_mastercard(22004000700000003)
    assert not is_mastercard(5624000000000013)
    assert not is_mastercard(2721000030000016)
    assert not is_mastercard(5101180000000000003)


if __name__ == "__main__":
    main()
