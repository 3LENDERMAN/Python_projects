from ib111 import week_05  # noqa


# Predicate ‹sum_to_exactly› returns if in ‹left› is element ‹x› and
# in list ‹right› some element ‹y› that ‹x + y == that›.

def sum_to_exactly(left: list[int], right: list[int], to: int) -> bool:
    for num in left:
        for num2 in right:
            if num + num2 == to: return True

    return False

# Predicate ‹sum_to_at_least› returns if in ‹left› is some element of ‹x› and in list ‹right›
# some element of ‹y› so it counts ‹x + y >= that›. Complexity should be linear.

def sum_to_at_least(left: list[int], right: list[int], at_least: int) -> bool:
    x = 0
    if left == [] or right == []: return False
    for num in right:
        if num > x: x = num
    if x >= at_least: return True
    for num2 in left:
        if x + num2 >= at_least: return True
    
    return False

# There is better way to solve this with complexity ⟦n⋅log n⟧ but it requires sorted lists.

def main() -> None: # run tests
    l1: list[int] = []
    l2 = [1, 20, 1, 3, -32, 5, 12, 4, 2, 33]
    l3 = [3, 232, 5, 2, 45, 34, 22, 4, 44]

    huge = [i for i in range(500000)]
    assert sum_to_exactly(l2, l3, 77)
    assert sum_to_exactly(l2, l3, 200)
    assert sum_to_exactly(huge, l2, 30)
    assert sum_to_exactly(l2, huge, 109090)
    assert not sum_to_exactly(l1, l2, 32)
    assert not sum_to_exactly(l2, l3, 150)
    assert not sum_to_exactly(huge, l2, 2000000)

    assert sum_to_at_least(l2, l3, 240)
    assert sum_to_at_least(huge, l2, 1000)
    assert sum_to_at_least(l3, huge, 400000)
    assert sum_to_at_least(huge, huge, 400000)
    assert not sum_to_at_least(l2, l3, 1000)
    assert not sum_to_at_least(l1, l3, 20)
    assert not sum_to_at_least(l2, l1, 20)
    assert not sum_to_at_least(huge, huge, 3000000)


if __name__ == "__main__":
    main()
