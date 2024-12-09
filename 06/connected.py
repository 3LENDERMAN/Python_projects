from ib111 import week_06  # noqa

# Consider a public transport system with named stops,
# between which (for us anonymous) connections run. The connections have a given direction:
# it is not guaranteed that if a connection goes from ⟦A⟧ to ⟦B⟧, then there is also a connection from ⟦B⟧ to
# ⟦A⟧. We will represent the transport network by a dictionary, where the key is
# some stop ⟦A⟧, and its corresponding value is a list
# of stops to which one can travel from ⟦A⟧ without stopping.

# The predicate decides whether it is possible to get
# from any stop to any other stop only by using
# connections from the given dictionary.

def all_connected(stops: dict[str, list[str]]) -> bool:
    if len(stops) == 1: return True
    are_joined: set[str] = set()
    for stop, dests in stops.items():
        changed = False
        for dest in dests:
            if dest in stops: are_joined.add(dest)
            changed = True
        if not changed: return False
    return len(stops) == len(are_joined)

def main() -> None:
    assert all_connected({"A": []})
    assert all_connected({"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]})
    assert all_connected({"A": ["B"], "B": ["C"], "C": ["D"], "D": ["A"]})
    assert all_connected({"A": ["B", "C", "D"], "B": ["C"], "C": ["A", "B"], "D": ["C"]})

    assert not all_connected({"A": ["B"], "B": []})
    assert not all_connected({"A": ["B", "C"], "B": ["C"], "C": ["B"]})
    assert not all_connected({"A": ["B", "C"], "B": ["C"], "C": ["B"]})
    assert not all_connected({"A": ["B", "C", "D"], "B": ["C"], "C": ["B"], "D": ["A"], "F": []})


if __name__ == '__main__':
    main()
