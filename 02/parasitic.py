from ib111 import week_02  # noqa

# ⟦k⟧-parasitic number in base ⟦b⟧ where ⟦b⟧ > 1 and ⟦k⟧ is number in interval from 1 to ⟦b - 1⟧)
# If numbers ⟦k⟧-multiple is created that his last digit in ⟦b⟧ base we move it to first place

# Example: ⟦179487⟧ is 4-parasitic in decimal, because ⟦179487 · 4 = 717948⟧; ⟦32⟧ is 
# 2-parasitic in 3-base, ⟦32 = (1012)₃⟧, ⟦32 · 2 = 64⟧ and ⟦64 = (2101)₃⟧.

# ‹is_parasitic› returns bool if ‹num› ⟦k⟧-parasitic in base ‹base› for some ⟦k⟧ – return ⟦k⟧ else None

def is_parasitic(num, base):
    length = get_length_in_base(num, base)

    last_digit = num % base
    shifted_num = (last_digit * (base ** (length - 1))) + (num // base)

    for k in range(1, base):
        if num * k == shifted_num:
            return k

    return None

def get_length_in_base(number, base):
    length = 0
    while number > 0:
        number //= base
        length += 1
    return length

def main() -> None: # run tests
    assert is_parasitic(1, 10) == 1
    assert is_parasitic(8, 7) == 1
    assert is_parasitic(63245, 42) == 1
    assert is_parasitic(179487, 10) == 4
    assert is_parasitic(12345, 10) is None
    assert is_parasitic(105263157894736842, 10) == 2
    assert is_parasitic(142857, 10) == 5
    assert is_parasitic(26144, 7) == 4
    assert is_parasitic(26144, 8) is None
    assert is_parasitic(314314, 12) == 8
    assert is_parasitic(83886, 16) == 11
    assert is_parasitic(
        1016949152542372881355932203389830508474576271186440677966, 10) == 6


if __name__ == "__main__":
    main()
