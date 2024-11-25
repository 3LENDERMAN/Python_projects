from ib111 import week_01  # noqa

# Consider sequence defined as ⟦a₁ = 1, aₙ₊₁ = aₙ ⋄ n⟧, where
# ⟦⋄⟧ is sequentially cycling among ⟦+, ⋅, -⟧. 

# First 5 values:
#  ⟦ a₁ = 1
#    a₂ = a₁ + 1 = 2
#    a₃ = a₂ ⋅ 2 = 4
#    a₄ = a₃ - 3 = 1
#    a₅ = a₄ + 4 = 5 ⟧

# This procedure calculates nth element of this cycle:
def cycle(n):
    # Index variable
    i = 1
    a_i = 1

    while i < n:
        if i % 3 == 1:
            a_i = a_i + i
        elif i % 3 == 2:
            a_i = a_i * i
        else:  # i % 3 == 0
            a_i = a_i - i

        i += 1

    return a_i

def main():  # demo
    assert cycle(1) == 1
    assert cycle(2) == 2
    assert cycle(3) == 4
    assert cycle(4) == 1
    assert cycle(5) == 5
    assert cycle(6) == 25
    assert cycle(7) == 19
    assert cycle(8) == 26


if __name__ == '__main__':
    main()
