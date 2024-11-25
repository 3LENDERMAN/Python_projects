from ib111 import week_01  # noqa

# Procedure returns value of the element ⟦aₙ⟧ of the following sequence.

# First element of the sequence is in ‹initial›,
# every other element is then based of ⟦aⱼ = ∑ᵢ₌₁ᵏ (-1)ⁱ · i · aⱼ₋₁⟧,

# For example, for ‹k = 3› a ‹initial = 2›:
#  ⟦ a₀ = 2
#    a₁ = ∑ᵢ₌₁³ (-1)ⁱ · i · a₀ = -a₀ + 2a₀ - 3a₀ = -2 + 4 - 6 = -4
#    a₂ = ∑ᵢ₌₁³ (-1)ⁱ · i · a₁ = -a₁ + 2a₁ - 3a₁ = 4 - 8 + 12 = 8 ⟧
# result should then be ‹8›.

def sequence(n, k, initial):
    if n == 0:
        return initial

    an = initial
    for _ in range(n):
        nextn = 0
        for i in range(1,(k+1)):
            nextn += (-1)**i * i * an
        
        an = nextn
    return an

def main():
    assert sequence(2, 3, 2) == 8
    assert sequence(0, 1, 7) == 7
    assert sequence(1, 1, 7) == -7
    assert sequence(1, 2, 7) == 7
    assert sequence(1, 3, 7) == -14
    assert sequence(3, 1, 1) == -1
    assert sequence(2, 2, 2) == 2
    assert sequence(5, 5, 2) == -486
    assert sequence(3, 10, 1) == 125
    assert sequence(4, 10, 1) == 625
    assert sequence(4, 4, 4) == 64


if __name__ == "__main__":
    main()
