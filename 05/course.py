from ib111 import week_05  # noqa

# Student grades for a single course are stored in a dictionary, where
# the key is the student's UČO and the value is the grade specified as a letter.
# Possible grades are 'A' to 'F', then 'N', 'P', 'X', 'Z' and '-'.

# ‹modus›, takes a dictionary of tokens and outputs their mode, i.e. the most frequent value.
# If the input dictionary is empty, the output will be an empty set.

def modus(marks: dict[int, str]) -> set[str]:
    most_frequent: set[str] = set()
    if len(marks) == 0: return most_frequent
    highest = 0
    count: dict[str,int] = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'N': 0, 'P': 0, 'X': 0, 'Z': 0, '-': 0}
    for uco, mark in marks.items():
        count[mark] += 1
        if count[mark] > highest: highest = count[mark]
    for grade, n in count.items():
        if n == highest: most_frequent.add(grade)
    return most_frequent

# Predicate ‹check› checks if grades are in right format: 
# (grades 'A' - 'F', or 'X'), (grades 'P', 'N'), (grades 'Z', 'N') or '-'

def check(marks: dict[int, str]) -> bool:
    #right_grades: set[str] = set()
    right_grades: set[str] = {'A', 'B', 'C', 'D', 'E', 'F', 'P', 'X', 'Z', '-'}
    for _, grade in marks.items():
        if grade not in right_grades: return False
    return True


def main() -> None: #run tests
    assert modus({}) == set()
    assert modus({100000: 'P'}) == {'P'}
    assert modus({100000: 'A', 100001: 'B', 100002: 'A'}) == {'A'}
    assert modus({100000: 'A', 100001: 'B', 100002: 'A', 100003: 'B'}) \
           == {'A', 'B'}
    assert check({})
    assert check({100000: 'P'})
    assert check({100000: '-'})
    assert check({100000: 'A', 100001: 'B', 100002: 'A'})
    assert check({100000: 'A', 100001: 'B', 100002: 'A', 100003: 'B'})
    assert not check({100000: 'A', 100001: 'B', 100002: 'A', 100003: 'N'})
    assert not check({100000: 'P', 100001: 'N', 100002: 'Z', 100003: '-'})


if __name__ == "__main__":
    main()
