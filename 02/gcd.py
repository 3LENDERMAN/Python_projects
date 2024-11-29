from ib111 import week_02  # noqa

# Clear function ‹gcd›, Finds for two numbers their greatest common divisor
# Basic naive algorithm (all possibilities)

def gcd(x1, x2):
    if x1 > x2:
        temp = x2
        x2 = x1
        x1 = temp
    for i in range(x1, 0, -1):
        if x1 % i == 0 and x2 % i == 0:
            return i

def main(): # run tests
    assert gcd(5, 5) == 5
    assert gcd(5, 10) == 5
    assert gcd(6, 15) == 3
    assert gcd(18, 15) == 3
    assert gcd(12, 1) == 1


if __name__ == "__main__":
    main()
