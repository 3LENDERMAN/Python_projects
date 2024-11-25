from ib111 import week_01  # noqa

# Clear function that calculates nth element of fibonacci sequence:
def fib(n):
    # <a> is penultimate and <b> last recently calculated fib. number
    a = 1
    b = 1

    # So far first two elements are calculated, to calculate next, we
    # add <(n-2)> to the sum and shift the variables to keep last two digits and empty the last
    for i in range(n - 2):
        c = a + b
        a = b
        b = c
    return b


def main():  # demo
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(5) == 5
    assert fib(9) == 34
    assert fib(11) == 89
    assert fib(20) == 6765
    assert fib(40) == 102334155
    for i in range(3, 100):
        assert fib(i) - fib(i - 1) == fib(i - 2)


if __name__ == "__main__":
    main()
