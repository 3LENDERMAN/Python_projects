from ib111 import week_01  # noqa

# Procedure returns sum of first ‹n› values of ‹k›-power 
# sum ⟦sₙ = ∑ᵢ₌₁ⁿ aᵢ⟧
# ⟦i⟧th element ⟦aᵢ = iᵏ⟧.

def powers(n, k):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** k
    return sum

def main():
    print(powers(3, 2))
    assert powers(3, 2) == 14
    assert powers(5, 2) == 55
    assert powers(5, 3) == 225
    assert powers(3, 10) == 60074
    assert powers(8, 1) == 36
    assert powers(170, 0) == 170
    assert powers(10, 7) == 18080425
    assert powers(125, 4) == 6226236975


if __name__ == "__main__":
    main()
