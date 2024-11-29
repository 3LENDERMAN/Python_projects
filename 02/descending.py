from ib111 import week_02  # noqa

# Function that checks if digits in number are descending in value.
# For example "321" or "775" is True but "123" is False

# ‹get_digit› gets digit value on k-index:
def get_digit(number, k):
    return (number // 10 ** k) % 10

# Each division by 10 "removes" one digit, thus in counter remains number of digits:
def count_digits(number):
    count = 0
    while number > 0:
        count += 1
        number = number // 10
    return count

# Main function that calls helper functions:
def is_descending(number):
    for k in range(count_digits(number) - 1):
        if get_digit(number, k + 1) < get_digit(number, k):
            return False

    return True

def main():  # Run simple tests
    assert is_descending(7)
    assert is_descending(321)
    assert is_descending(33222111)
    assert is_descending(9999)
    assert is_descending(7741)
    assert not is_descending(123)
    assert not is_descending(332233)
    assert not is_descending(774101)

if __name__ == "__main__":
    main()