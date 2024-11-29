from ib111 import week_02  # noqa

# ‹count_digit_in_sequence›, returns how many times ‹digit› 
# occurs in numbers in interval from <low> to <hight> including.

def count_digit_in_sequence(digit, low, high):
    counter = 0
    for i in range(low, high + 1):
        for x in range(1, count_digits(i) + 1):
            if get_digit(i, x) == digit:
                counter += 1
    
    return counter

def count_digits(number):
    counter = 0
    if number == 0:
        return 1
    while number > 0:
        number //= 10
        counter += 1
    return counter

def get_digit(number, index):
    digit = 0
    while index > 0:
        digit = number % 10
        number //= 10
        index -= 1
    return digit 

def main(): # run tests
    assert count_digit_in_sequence(1, 0, 13) == 6
    assert count_digit_in_sequence(0, 10, 20) == 2
    assert count_digit_in_sequence(0, 0, 10) == 2
    assert count_digit_in_sequence(4, 15, 23) == 0
    assert count_digit_in_sequence(5, 20, 120) == 20
    assert count_digit_in_sequence(0, 10, 100) == 11
    assert count_digit_in_sequence(2, 111, 1000) == 279


if __name__ == "__main__":
    main()
