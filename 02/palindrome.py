from ib111 import week_02  # noqa


# Predicate that checks if number is palindrome
# That means it´s read same way from left or right

def is_palindrome(number):
    if number < 10:
        return True
    n = count_digits(number)
    index = 1
    while index <= count_digits(number) // 2: 
        first = get_digit(n, number)
        last = get_digit(index, number)
        if first != last:
            return False
        n -= 1
        index += 1
    return True
    
def count_digits(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count

def get_digit(index, number):
    value = 0
    while index > 0:
        value = number % 10
        number //= 10
        index -= 1
    return value

def main(): # run simple tests
    assert is_palindrome(7)
    assert is_palindrome(1221)
    assert is_palindrome(12121)
    assert not is_palindrome(1212)
    assert not is_palindrome(12345)


if __name__ == "__main__":
    main()
