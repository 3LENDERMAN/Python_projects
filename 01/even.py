from ib111 import week_01  # noqa

# Sequence of ⟦aᵢ⟧ to the power of 2 even numbers ⟦aᵢ = 4i²⟧.
# Function returns sum of the first n elements -> ⟦sₙ = ∑ᵢ₌₁ⁿ aᵢ = ∑ᵢ₌₁ⁿ 4i²⟧.

def even(n):
    sumNum = 0
    index = 2
    while n > 0:
        if index ** 2 % 2 == 0:
            sumNum += index ** 2
            n -= 1
        index += 1

    return sumNum

def main():
    assert even(1) == 4
    assert even(2) == 20
    assert even(3) == 56
    assert even(4) == 120
    assert even(10) == 1540
    assert even(134) == 3244140


if __name__ == "__main__":
    main()
