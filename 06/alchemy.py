from ib111 import week_06  # noqa

# We will find out if it is possible to produce
# the desired substance using alchemy. The input is:
#
# • a set of substances that you already have (if you already have
#   a substance, you have it available in unlimited quantities),
# • a dictionary that determines how existing substances
#   can be transmuted: the key is the substance that we can create and
#   the value is the list of "input" substances that we need to produce
# • the target substance that we are trying to produce.
#
# a predicate whose value will be ‹True› if the desired substance can be created from the given
# substances according to the given rules,
# ‹False› otherwise.

def is_creatable(owned_substances: set[str], rules: dict[str, set[str]], wanted: str) -> bool:
    if len(rules) == 0 and wanted in owned_substances: return True
    create_all: set[str] = owned_substances.copy()
    for substance, needed in rules.items():
        is_present = True
        for sub in needed:
            if sub not in create_all:
                is_present = False
        if is_present: create_all.add(substance)
        if wanted in create_all: return True
    return False

def main() -> None:
    assert is_creatable({"a"}, {}, "a")
    assert is_creatable({"a", "b"}, {"c": {"a", "b"}}, "c")
    assert is_creatable({"a", "b"}, {"c": {"a"}, "d": {"c"}}, "d")
    assert is_creatable({"a", "b"}, {"c": {"a", "b"}, "d": {"a", "c"},
                                     "e": {"d", "b"}, "f": {"e", "a"}}, "f")

    owned = {"b", "c", "d"}
    rules = {"a": {"b", "c", "d"},
             "e": {"a", "b", "c", "d"},
             "f": {"a", "b", "c", "d", "e"}}

    assert is_creatable(owned, rules, "f")
    assert owned == {"b", "c", "d"}
    assert rules == {"a": {"b", "c", "d"},
                     "e": {"a", "b", "c", "d"},
                     "f": {"a", "b", "c", "d", "e"}}

    assert not is_creatable({"a"}, {"c": {"a", "b"}}, "c")
    assert not is_creatable(set(), {"c": {"a", "b"}}, "c")
    assert not is_creatable({"a", "b"}, {}, "c")

    owned = {"a", "b"}
    rules = {"c": {"a", "b"}, "d": {"a", "c"},
             "e": {"d", "b"},
             "f": {"e", "a", "h"}}
    assert not is_creatable(owned, rules, "f")
    assert owned == {"a", "b"}
    assert rules == {"c": {"a", "b"}, "d": {"a", "c"},
                     "e": {"d", "b"},
                     "f": {"e", "a", "h"}}


if __name__ == '__main__':
    main()
