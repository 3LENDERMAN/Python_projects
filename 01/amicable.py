from ib111 import week_01  # noqa

# Predicate that determines if 2 numbers are friends
# (amicable). Friendly numbers are two natural numbers such that
# that the sum of all proper divisors of a number is equal
# to the second number, and vice versa – the sum of all proper divisors
# of the second number is equal to the first.
#
# We consider all of its positive divisors to be proper divisors of a number
# of divisors excluding the number itself; e.g. own divisors
# 12 numbers are 1, 2, 3, 4, 6.
def amicable(a, b):
    return is_abundant(a) == b and is_abundant(b) == a

def is_abundant(number):
    count = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            count += i

    return count

def main():
    assert not amicable(136, 241)
    assert not amicable(1, 1)
    assert amicable(220, 284)
    assert amicable(1184, 1210)
    assert amicable(2620, 2924)
    assert not amicable(1190, 1212)
    assert not amicable(349, 234)


if __name__ == "__main__":
    main()
