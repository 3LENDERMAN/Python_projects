from ib111 import week_01  # noqa

# This procedure returns number of different divisors of the whole number <number>
def divisors(number):
    n = 1
    count = 1
    while n < number:
        n += 1
        if number % n == 0:
            count += 1
    return count

def main():
    assert divisors(1) == 1
    assert divisors(2) == 2
    assert divisors(3) == 2
    assert divisors(4) == 3
    assert divisors(5) == 2
    assert divisors(12) == 6
    assert divisors(16) == 5
    assert divisors(18) == 6
    assert divisors(42) == 8
    assert divisors(100) == 9
    assert divisors(127) == 2
    assert divisors(1024) == 11
    assert divisors(1069) == 2


if __name__ == "__main__":
    main()
