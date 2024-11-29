from ib111 import week_02  # noqa

# Consider twelve base ⟦0, 1, 2, 3, 4, 5, 6, 7, 8, 9⟧ and also ⟦δ⟧ (as 10), ⟦ε⟧ (as 11).
#
# Shuffle operation: digits ⟦δ⟧ on left and ⟦ε⟧ on right all other numbers remain, 
# ‹zwelf_shuffle(num)›, gets number > 0 and returns value after the shuffle op.

# Examples:
# • 3302 in 12-base ⟦(1δε2)ᵦ⟧ after shuffle ⟦(δ12ε)ᵦ = 17459⟧,
# • 1587 in 12-base ⟦(ε03)ᵦ⟧ after shuffle ⟦(03ε)ᵦ = 47⟧,
# • 1729 in 12-base ⟦(1001)ᵦ⟧ no shuffle.

def zwelf_shuffle(num):
    normal_part = 0  
    tens_count = 0   
    elevens_count = 0  
    place_value = 1  

    # Iterate through every digit in num
    while num > 0:
        digit = num % 12  # Digit in 12-base
        num //= 12  # Shift digit for another iteration
        if digit == 10:  # 'δ'
            tens_count += 1
        elif digit == 11:  # 'ε'
            elevens_count += 1
        else:
            normal_part += digit * place_value
            place_value *= 12  

    while tens_count > 0:
        normal_part += 10 * place_value
        place_value *= 12
        tens_count -= 1

    while elevens_count > 0:
        normal_part += 11 * place_value
        place_value *= 12
        elevens_count -= 1

    return normal_part

def main() -> None: # run simple tests
    assert zwelf_shuffle(3302) == 17459
    assert zwelf_shuffle(1587) == 47
    assert zwelf_shuffle(1451) == 1451


if __name__ == '__main__':
    main()
