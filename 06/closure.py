from ib111 import week_06  # noqa

# Consider the representation ⟦f: A × A → A⟧ where ⟦A ⊆ ℤ⟧ and ⟦f⟧ is given by
# a table (a dictionary where the key is a pair of numbers and the value is a number
# – consider that such a dictionary really represents a table,
# if all the necessary pairs are present in the dictionary).
# For example, the logical conjunction ‹and› can be represented by a similar table
# as follows (if we represent ‹True› by the number 1 and
# ‹False› by the number 0):
# │   │ 0 │ 1 │
# ├── │── ┼── │
# │ 0 │ 0 │ 0 │
# │ 1 │ 0 │ 1 │

# The table represented by dictionary:
#     {(0, 0): 0, (0, 1): 0,
#      (1, 0): 0, (1, 1): 1}.
#
# We will call the representation ⟦f⟧ an «operation» and describe it
# with the following type:

Operation = dict[tuple[int, int], int]

# The input is a table that represents ⟦f⟧ and a set
# of numbers ⟦B ⊆ A⟧. Our task will be to find the smallest set of numbers ⟦C⟧
# such that:
# • ⟦B ⊆ C⟧, i.e. C contains all the given elements,
# • for each ⟦(x, y) ∈ B × B⟧ ⟦f(x, y) ∈ B⟧ – ⟦C⟧ is «closed» under operation ⟦f⟧.

def closure(set_b: set[int], operation_f: Operation) -> set[int]:
    set_c = set_b.copy()

    to_add = find_missing(set_c, operation_f)

    while len(to_add) != 0:
        for x in to_add:
            set_c.add(x)
        to_add = find_missing(set_c, operation_f)

    return set_c

# Help function ‹find_missing› goes through all tuples from ⟦C × C⟧ (product of set 
# ‹set_c› and ‹set_c›),and if this pair appears on an element that is not yet in ‹set_c›
# it adds it to its return value.

def find_missing(set_c: set[int], operation_f: Operation) \
        -> set[int]:
    result: set[int] = set()

    for x in set_c:
        for y in set_c:
            to_add = operation_f[(x, y)]
            if to_add not in set_c:
                result.add(to_add)

    return result

def main() -> None:  # tests
    op_and = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 1}
    op_xor = {(0, 0): 0, (1, 0): 1, (0, 1): 1, (1, 1): 0}
    set_false = set([0])
    set_true = set([1])
    set_both = set([0, 1])

    assert closure(set_false, op_and) == set_false
    assert closure(set_true, op_and) == set_true
    assert closure(set_both, op_and) == set_both
    assert closure(set_false, op_xor) == set_false
    assert closure(set_true, op_xor) == set_both

    add_mod4 = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3,
                (1, 0): 1, (1, 1): 2, (1, 2): 3, (1, 3): 0,
                (2, 0): 2, (2, 1): 3, (2, 2): 0, (2, 3): 1,
                (3, 0): 3, (3, 1): 0, (3, 2): 1, (3, 3): 2}

    assert closure(set([0]), add_mod4) == set([0])
    assert closure(set([1]), add_mod4) == set([0, 1, 2, 3])
    assert closure(set([2]), add_mod4) == set([0, 2])
    assert closure(set([3]), add_mod4) == set([0, 1, 2, 3])
    assert closure(set([0, 2]), add_mod4) == set([0, 2])


if __name__ == '__main__':
    main()
