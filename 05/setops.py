from ib111 import week_05  # noqa


# Simple set operation without using functions.

# Union operation makes set that has all elements from both sets.
def set_union(a: set[int], b: set[int]) -> set[int]:
    union = set()
    for n in a: union.add(n)    
    for n in b: union.add(n)
    return union

def set_update(to_extend: set[int], other: set[int]) -> None:
    for num in other:
        to_extend.add(num)

# Intersection makes set that consists of elements which are in both sets.
def set_intersect(a: set[int], b: set[int]) -> set[int]:
    intersect = set()
    for num in a:
        for num2 in b:
            if num == num2:
                intersect.add(num)
    return intersect

def set_keep(to_reduce: set[int], other: set[int]) -> None:
    x:set[int] = set()
    for num in to_reduce:
        if num not in other:
            x.add(num)
    for n in x: 
        to_reduce.remove(n)

def main() -> None: # run tests
    x = {1}
    y = {2}

    assert set_union(x, y) == {1, 2}
    assert x == {1}
    assert y == {2}

    set_update(x, y)
    assert x == {1, 2}
    assert y == {2}

    assert set_intersect(x, y) == {2}
    assert x == {1, 2}
    assert y == {2}

    set_keep(x, y)
    assert x == {2}
    assert y == {2}

    for i in range(1000):
        x.add(i)

    set_update(x, y)
    assert len(x) == 1000

    set_update(y, x)
    assert x == y

    set_keep(x, y)
    assert x == y

    assert set_intersect(x, y) == x
    y.remove(33)
    assert set_intersect(x, y) == y
    assert set_union(x, y) == x


if __name__ == '__main__':
    main()
