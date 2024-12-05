from ib111 import week_05  # noqa


# set difference operation (set with elements only in first set and not in second)
def set_difference(a: set[int], b: set[int]) -> set[int]:
    diff: set[int] = set()
    for num in a:
        if num not in b:
            diff.add(num)
    return diff


def set_remove(to_reduce: set[int], other: set[int]) -> None:
    to_remove:set[int] = set()
    for num in to_reduce:
        if num in other:
            to_remove.add(num)
    for x in to_remove:
        to_reduce.remove(x)


# symmetrical difference has all elements that are not in both sets.
def set_symmetric_diff(a: set[int], b: set[int]) -> set[int]:
    diff:set[int] = set()
    for num in a:
        if num not in b:
            diff.add(num)
    for num in b:
        if num not in a:
            diff.add(num)
    return diff


def set_symmetric_inplace(to_change: set[int],
                          other: set[int]) -> None:
    to_remove: set[int] = set()
    for num in to_change:
        if num in other:
            to_remove.add(num)
    for num in other:
        if num not in to_change:
            to_change.add(num)
    for x in to_remove:
        to_change.remove(x)


def main() -> None: # run tests
    x = {1}
    y = {2}

    assert set_difference(x, y) == x
    assert set_difference(y, x) == y
    assert x == {1}
    assert y == {2}

    set_remove(x, y)
    assert x == {1}
    assert y == {2}

    x.add(2)

    assert set_difference(x, y) == {1}
    assert set_difference(y, x) == set()

    set_remove(x, y)
    assert x == {1}
    assert y == {2}

    assert set_symmetric_diff(x, y) == {1, 2}
    x.add(2)
    assert set_symmetric_diff(x, y) == {1}
    y.add(3)
    assert set_symmetric_diff(x, y) == {1, 3}
    y.add(4)
    assert set_symmetric_diff(x, y) == {1, 3, 4}

    set_symmetric_inplace(x, y)
    assert x == {1, 3, 4}
    assert y == {2, 3, 4}

    set_symmetric_inplace(x, y)
    assert x == {1, 2}
    assert y == {2, 3, 4}


if __name__ == '__main__':
    main()
