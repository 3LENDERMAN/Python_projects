from ib111 import week_04  # noqa


# The Fibonacci numbers use the Fibonacci system to write positive integers.
# It uses only two digits, 0 and 1; however, the order of the numbers is not a power of two
# as in the classic binary system, but is sequentially from the right 1, 2, 3, 5,
# 8, 13, … (These are Fibonacci numbers without the leading 0 and 1.)
# Some numbers can be written in two different ways, for example, the number
# ⟦17⟧ is written either as ⟦(100101)ᵩ⟧ or as ⟦(11101)ᵩ⟧.
# The following holds: ⟦17 = 13 + 3 + 1 = 8 + 5 + 3 + 1⟧.
# Therefore, the so-called «canonical notation» of a number in the Fibonacci system,
# where it is forbidden to have two ones next to each other.
#
# The pure function ‹fib_ones› calculates how many ones there are in the canonical
# Fibonacci notation of a non-negative integer ‹num›.
#
# Examples:
# In the canonical Fibonacci notation of the number ⟦17⟧ there are three ones, see above.
# In the canonical Fibonacci notation of the number ⟦34⟧ there is one one (it is
# a Fibonacci number).
# In the canonical Fibonacci notation of the number ⟦101⟧ there are four ones, because
# ⟦101 = 89 + 8 + 3 + 1⟧ holds.

def fib_ones(num: int) -> int:
    l = [1, 2]
    while num > l[len(l) - 1]:
        l.append(l[len(l) - 2] + l[len(l) - 1])
    ones = 0
    for x in range(len(l) - 1, -1, -1):
        if num >= l[x]:
            num -= l[x]
            ones += 1
    return ones

def main() -> None:
    assert fib_ones(1) == 1
    assert fib_ones(3) == 1
    assert fib_ones(17) == 3
    assert fib_ones(34) == 1
    assert fib_ones(101) == 4
    assert fib_ones(2022) == 5
    assert fib_ones(123456789) == 12


if __name__ == '__main__':
    main()
