from ib111 import week_06  # noqa


# A given natural number is «b–lucky» if it is true that if we replace it
# with the sum of the squares of its digits, expressed in the positional system
# with base ‹b›, and we repeat this procedure on the thus
# formed number, after a finite number of steps we get the number 1.

# For example, the number 3 is 4–lucky because:
#
# • ⟦3 = (3)₄⟧
# • ⟦3² = 9 = (21)₄⟧
# • ⟦2² + 1² = 5 = (11)₄⟧
# • ⟦1² + 1² = 2 = (2)₄⟧
# • ⟦2² = 4 = (10)₄⟧
# • ⟦1² + 0² = 1⟧.
#
# The number 2 is not 5–lucky:
#
# • ⟦2 = (2)₅⟧
# • ⟦2² = 4 = (4)₅⟧
# • ⟦4² = 16 = (31)₅⟧
# • ⟦3² + 1² = 10 = (20)₅⟧
# • ⟦2² + 0² = 4⟧
#
# and since the number 4 was repeated in the calculation, we can no longer get
# to the result 1.

# A predicate that decides whether the number ‹number› is
# ‹base›-lucky.

def is_b_happy(number: int, base: int) -> bool:
    dont_repetate: set[int] = set()
    num = number
    while num != 1:
        if num in dont_repetate: return False
        dont_repetate.add(num)
        temp = num
        num = 0
        while temp > 0:
            num += (temp % base) ** 2
            temp //= base
    return True

def main() -> None: # tests
    assert is_b_happy(3, 4)
    assert is_b_happy(11, 11)
    assert is_b_happy(19, 10)
    assert is_b_happy(347, 6)
    assert is_b_happy(123456, 4)
    assert is_b_happy(7, 10)

    assert not is_b_happy(2, 5)
    assert not is_b_happy(20, 6)
    assert not is_b_happy(100, 5)
    assert not is_b_happy(125, 10)
    assert not is_b_happy(40, 10)
    assert not is_b_happy(8, 6)
    assert not is_b_happy(15, 16)

if __name__ == '__main__':
    main()
