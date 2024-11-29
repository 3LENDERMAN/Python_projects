from ib111 import week_03  # noqa

# Predicate ‹all_greater_than›, returns True when all numbers 
# in ‹sequence› are bigger than ‹n›.
def all_greater_than(sequence, n):
    for num in sequence:
        if num <= n:
            return False
    return True

# Predicate ‹any_even›, is True when there is odd number in ‹sequence›:
def any_even(sequence):
    for num in sequence:
        if num % 2 == 0:
            return True
    return False

def main(): # run tests
    assert all_greater_than([1, 2, 0, -1, 1, 14], -3)
    assert not all_greater_than([1, 2, 0, -1, 1, 14], 14)
    assert all_greater_than([], -100)
    assert all_greater_than([], 100)
    assert all_greater_than([12, 21, 14, 10], 7)
    assert all_greater_than([1, 2, 14, 10], -25)
    assert not all_greater_than([-5, -6, -10, -9], -4)
    assert all_greater_than([-5, -6, -10, -9], -40)

    assert not any_even([])
    assert any_even([2])
    assert any_even([1, 2])
    assert not any_even([1, 3])


if __name__ == "__main__":
    main()
