from ib111 import week_01  # noqa

# Let´s consider sequence:
#  ⟦aₙ = nⁿ⟧
#
# and sequence of theirs partition sums  
#  ⟦sₙ = ∑ᵢ₌₁ⁿ aᵢ = ∑ᵢ₌₁ⁿ iⁱ⟧
#  ⟦ a₁ = 1¹ = 1
#    a₂ = 2² = 4
#    a₃ = 3³ = 27 ⟧

#  ⟦ s₁ = ∑ᵢ₌₁¹ iⁱ = 1¹           = 1          = 1
#    s₂ = ∑ᵢ₌₁² iⁱ = 1¹ + 2²      = 1 + 4      = 5
#    s₃ = ∑ᵢ₌₁³ iⁱ = 1¹ + 2² + 3³ = 1 + 4 + 27 = 32 ⟧

# This clear function calculates value of ⟦aₙ⟧nth element of the sequence:  
def nth_element(n):
    return n ** n


def partial_sum(n):
    # Keep adding to "result values of ⟦aᵢ⟧"
    result = 0

    for i in range(n):
        result += nth_element(i + 1)

    # After the iterations, there is wanted sum: 
    # ⟦sₙ = ∑ᵢ₌₁ⁿ aᵢ⟧
    return result


def main():  # demo
    print(partial_sum(5))
    assert partial_sum(1) == 1
    assert partial_sum(2) == 5
    assert partial_sum(3) == 32
    assert partial_sum(4) == 288
    assert partial_sum(7) == 873612
    assert partial_sum(15) == 449317984130199828


if __name__ == "__main__":
    main()
