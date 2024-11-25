from ib111 import week_01  # noqa

# Predicate ‹is_abundant› is true if it is number 
# ‹number› abundant, i.e. is less than the sum of its of own divisors.
#
# All of its positive divisors are proper divisors of a number
# of divisors excluding the number itself; e.g. own divisors
# 12 numbers are 1, 2, 3, 4, 6.

def is_abundant(number):
    count = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            count += i

    return count > number

def main():
    assert is_abundant(12)
    assert is_abundant(18)
    assert is_abundant(20)
    assert is_abundant(24)
    assert is_abundant(36)
    assert is_abundant(100)
    assert is_abundant(120)

    assert not is_abundant(7)
    assert not is_abundant(15)
    assert not is_abundant(55)
    assert not is_abundant(62)
    assert not is_abundant(130)


if __name__ == "__main__":
    main()
