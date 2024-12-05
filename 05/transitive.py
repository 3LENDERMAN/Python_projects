from ib111 import week_05  # noqa


# Binary relation is set of all tuples of relation. 
# Relation is transitive when all tuples in relation ⟦(a, b), (b, c)⟧ that there is also ⟦(a, c)⟧

# Predicate tells if relation is transitive.
def is_transitive(relation: set[tuple[int, int]]) -> bool:
    if len(relation) < 2: return True
    for (a, b) in relation:
        for (x, y) in relation:
            if b == x: 
                if (a, y) not in relation: return False
    return True


def main() -> None: # run tests
    assert is_transitive({(1, 2)})
    assert is_transitive(set())
    assert is_transitive({(1, 2), (2, 1), (1, 1), (2, 2)})
    assert is_transitive({(1, 2), (2, 3), (1, 3)})

    assert not is_transitive({(1, 2), (2, 3)})
    assert not is_transitive({(1, 2), (2, 1)})
    assert not is_transitive({(1, 2), (2, 5), (5, 1)})
    assert not is_transitive({(1, 5), (5, 6), (6, 1)})


if __name__ == '__main__':
    main()
