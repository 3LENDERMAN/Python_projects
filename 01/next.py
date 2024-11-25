from ib111 import week_01  # noqa

# Function returns for a given integer ‹number› finds 
# the nearest larger number that is a positive multiple integers ‹k›.

def next_multiple(number, k):
    num = 0
    while num == 0:
        number += 1
        if number % k == 0:
            num = number

    return num

# Function that for a given positive integer
# ‹number› finds the nearest larger prime number

def next_prime(number):
    while True:
        number += 1
        if is_prime(number):
            return number

def is_prime(num):
    if num < 2: return False

    for i in range(2, num):
        if num % i == 0: return False

    return True

def main():
    assert next_multiple(1, 2) == 2
    assert next_multiple(10, 7) == 14
    assert next_multiple(10, 5) == 15
    assert next_multiple(54, 6) == 60
    assert next_multiple(131, 29) == 145
    assert next_multiple(123, 112) == 224
    assert next_multiple(423, 90) == 450

    assert next_prime(1) == 2
    assert next_prime(2) == 3
    assert next_prime(3) == 5
    assert next_prime(4) == 5
    assert next_prime(11) == 13
    assert next_prime(12) == 13
    assert next_prime(13) == 17


if __name__ == "__main__":
    main()
