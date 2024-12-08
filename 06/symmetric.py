from ib111 import week_06  # noqa

# predicate whose value will be ‹True› if
# it receives a symmetric relation in the parameter, ‹False› otherwise.

def is_symmetric(relation: set[tuple[int, int]]) -> bool:
    if relation == set(): return True
    for (x, y) in relation:
        if (y, x) not in relation:
            return False
    return True


def main() -> None:
    assert is_symmetric({(1, 2), (2, 1)})
    assert is_symmetric(set())
    assert is_symmetric({(1, 2), (3, 4), (4, 3), (2, 1)})

    assert not is_symmetric({(1, 2)})
    assert not is_symmetric({(1, 2), (2, 3)})
    assert not is_symmetric({(1, 2), (3, 4), (2, 3), (4, 5)})


if __name__ == '__main__':
    main()
