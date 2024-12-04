from ib111 import week_04  # noqa
from math import pi, isclose

# Basic typing..

def degrees(radians: float) -> float:
    return (radians * 180) / pi


# ‹to_list› splits and converts numbers by the corresoinding base.

def to_list(num: int, base: int) -> list[int]:
    digits = []
    result = []

    while num > 0:
        digits.append(num % base)
        num //= base

    for i in range(len(digits)):
        result.append(digits[-i - 1])

    return result

# ‹diagonal› creates values on diagonal of ‹matrix›.

def diagonal(matrix: list[list[int]]) -> list[int]:
    diag = []
    for i in range(len(matrix)):
        diag.append(matrix[i][i])
    return diag

def with_id(elements: list[tuple[int, str]], id_: int) -> str | None:
    for element_id, val in elements:
        if id_ == element_id:
            return val
    return None

def update_students(students: list[tuple[int, str, int | None]], end: int) -> list[tuple[int, str, int]]:
    result = []

    for uco, name, graduated in students:
        if graduated is None:
            graduated = end
        result.append((uco, name, graduated))

    return result

# ‹is_increasing› is True when ‹seq› is ascending.

def is_increasing(seq: list[int]) -> bool:
    for i in range(1, len(seq)):
        if seq[i - 1] >= seq[i]:
            return False
    return True


def main() -> None:
    assert isclose(degrees(pi), 180)
    assert isclose(degrees(pi / 6), 30)

    assert diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 5, 9]

    assert to_list(123, 10) == [1, 2, 3]

    assert with_id([(1, 'a'), (2, 'b'), (3, 'c')], 2) == 'b'

    assert update_students([(123456, "Adam", 2018),
                            (123457, "Eva", None)], 2020) == \
        [(123456, "Adam", 2018),
         (123457, "Eva", 2020)]

    assert is_increasing([1, 2, 3])
    assert not is_increasing([1, 3, 2])


if __name__ == "__main__":
    main() 
