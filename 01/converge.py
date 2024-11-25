from ib111 import week_01  # noqa
from math import sin

# Function calculates Subsequence of the main sequence
# where subsequence is created by skipping elements 
# followed by certain rule:
#  ⟦ A → 1, 2, 3, 4, 5, …
#    B → 1,    3,    5, … ⟧ -> subsequence rule: only odd values

# Convergent sequence is sequence where element values are slowly 
# approaches the value of "limit" as ⟦L⟧

# This function finds value of nth element of this subsequence: 
def convergent(n):
    # We need two index variables
    i = 1
    j = 1

    # Last remembered value:
    last = sin(i)

    while j < n:
        i += 1
        if sin(i) > 0 and sin(i) <= last:
            j += 1
            last = sin(i)

    return last


def main():  # demo
    assert convergent(1) == sin(1)
    assert convergent(2) == sin(3)
    assert convergent(3) == sin(44)
    print(sin(1))
    print(sin(3))
    print(sin(44))
    
    for i in range(5):
        assert convergent(i + 1) <= convergent(i)
        assert convergent(i) > 0


if __name__ == '__main__':
    main()
