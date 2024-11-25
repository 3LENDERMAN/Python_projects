from ib111 import week_01  # noqa

# Let ⟦A⟧ be a Fibonacci sequence with terms ⟦aₙ⟧ and ⟦B⟧ be
# a sequence such that it has the ⟦aᵢ⟧th element at the ⟦i⟧th position
# of sequences ⟦A⟧, i.e. element with index ⟦aᵢ⟧ 
# Function sums the first ‹count› elements of sequences ⟦B⟧.

# For example:
#  ⟦ a₁ + a₁ + a₂ + a₃ + a₅ + a₈ = 1 + 1 + 1 + 2 + 5 + 21 = 31 ⟧

def fibfibsum(count):
    a = 0
    b = 1
    sumNum = 1
    while count - 1 > 0:
        ca = a + b
        a = b
        b = ca
        sumNum += fib(b)
        count -= 1

    return sumNum   

def fib(nth):
    a = 0
    b = 1
    while nth - 1 > 0:
        c = a + b
        a = b
        b = c
        nth -= 1

    return b


def main():
    assert fibfibsum(3) == 3
    assert fibfibsum(5) == 10
    assert fibfibsum(6) == 31
    assert fibfibsum(7) == 264
    assert fibfibsum(10) == 139589576542


if __name__ == "__main__":
    main()
