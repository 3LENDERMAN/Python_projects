from ib111 import week_05  # noqa

#‹image›, takes a dictionary ‹f›, which represents a representation, and a set ‹values›.
# The result is an image of the set ‹values› – that is, a set of values ​​on which
# the values ​​from the set ‹values› are displayed.

def image(f: dict[int, int], values: set[int]) -> set[int]:
    set_val: set[int] = set()
    for key, val in f.items():
        if key in values:
            set_val.add(val)
    return set_val

# Similarly, the function ‹preimage› computes the pattern of the given set ‹values›
# (the set of values ​​that ‹f› maps to some element of the set
# ‹values›):

def preimage(f: dict[int, int], values: set[int]) -> set[int]:
    set_val: set[int] = set()
    for key, val in f.items():
        if val in values:
            set_val.add(key)
    return set_val

# ‹compose›, the input will be two maps (dictionaries) ‹f› and ‹g› and the output will be a dictionary
# representing the map ‹f ∘ g›. The input condition is that ‹f› is
# defined for every value of the map ‹g›.

def compose(f: dict[int, int], g: dict[int, int]) -> dict[int, int]:
    x: set[tuple[int,int]] = set()
    temp_dict: dict[int,int] = dict(x)
    for key, val in g.items():
        for key2, val2 in f.items():
            if val == key2:
                temp_dict[key] = val2
    return temp_dict

# ‹kernel›, the input will be the mapping (dictionary) ‹f› and the result will be an equivalence relation ⟦R⟧
# (set of pairs) such that ⟦(x, y) ∈ R⟧ if and only if ⟦f(x) = f(y)⟧.

def kernel(f: dict[int, int]) -> set[tuple[int, int]]:
    value_groups: dict[int, list[int]] = {}
    for key, val in f.items():
        if val not in value_groups:
            value_groups[val] = []
        value_groups[val].append(key)
    
    # Create set of tuples based on groups
    result: set[tuple[int, int]] = set()
    for group in value_groups.values():
        # For each group create tuples
        for i in range(len(group)):
            for j in range(i, len(group)):
                result.add((group[i], group[j]))  # add (x, y)
                result.add((group[j], group[i]))  # add (y, x) for symmetry
    return result

def main() -> None: # run tests
    f = {1: 1, 2: 2}
    g = {1: 2, 2: 1}
    h = {1: 2, 2: 2}

    assert image(f, {1}) == {1}
    assert image(g, {1}) == {2}
    assert image(h, {1, 2}) == {2}

    assert preimage(f, {1}) == {1}
    assert preimage(f, {1, 2}) == {1, 2}
    assert preimage(g, {1}) == {2}
    assert preimage(h, {2}) == {1, 2}

    assert compose(f, g) == g
    assert compose(g, f) == g
    assert compose(h, g) == h
    assert compose(h, h) == h
    assert compose(g, g) == f

    assert kernel(f) == {(1, 1), (2, 2)}
    assert kernel(g) == {(1, 1), (2, 2)}
    assert kernel(h) == {(1, 1), (2, 2), (1, 2), (2, 1)}

    f = {1: 1, 2: 1, 3: 2}
    assert kernel(f) == {(1, 1), (2, 2), (3, 3),
                         (1, 2), (2, 1)}


if __name__ == '__main__':
    main()
