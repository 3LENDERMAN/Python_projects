from ib111 import week_01  # noqa

# Function nested returns nth element of the sequence (from 0) which 
# is created by adding gradually larger prefixes of natural numbers 

# Let ⟦Aᵢ⟧ is sequence from ⟦1⟧ to ⟦i⟧:
#
#  ⟦ A₁ → 1
#    A₂ → 1, 2
#    A₃ → 1, 2, 3
#    A₄ → 1, 2, 3, 4
#    A₅ → 1, 2, 3, 4, 5 ⟧
#
# Sequence ⟦B⟧ is then created from chaining ⟦A₁⟧, ⟦A₂⟧,
# ⟦A₃⟧ … to infinity
#  ⟦ B  → 1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, … ⟧
# This function finds nth element of such sequence:
def nested(n):
    length = 0  
    i = 1   

    while length + i <= n:
        length += i  # Add length of current sequence Aᵢ
        i += 1       # Shift to next sequnce (A₁ → A₂ → A₃ → ...)
        
    return (n - length) + 1

# This function then calculates sum of first n values: 
def nested_sum(n):
    length = 0  
    i = 1   
    summ = 0

    while length + i <= n:
        # Add sum of all values in current prefix
        for x in range(1, i + 1):
            summ += x       
        length += i  
        i += 1       # Shift to next sequence

    # Add elements which are in remaining part:
    for x in range(1, (n - length) + 1):
        summ += x

    return summ

def main():
    assert nested(0) == 1
    assert nested(1) == 1
    assert nested(2) == 2
    assert nested(8) == 3
    assert nested(9) == 4
    assert nested(25) == 5
    assert nested(130) == 11

    assert nested_sum(2) == 2
    assert nested_sum(5) == 7
    assert nested_sum(13) == 26
    assert nested_sum(30) == 87
    assert nested_sum(100) == 500


if __name__ == "__main__":
    main()
