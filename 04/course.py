from ib111 import week_04  # noqa

# Course is represented by tuples (student, grade)
# student is triple (id, name, semester) and grade ‹A› to ‹F›.

# ‹failed› list of students of ‹course› who got ‹F›.
Student = tuple[int, str, int]

def failed(course: list[tuple[Student, str]]) -> list[Student]:
    failiures = []
    for student in course:
        info, grade = student
        if grade == "F":
            failiures.append(info)
    return failiures

# ‹count_passed› , returns number of students who finished ‹course›
def count_passed(course: list[tuple[Student, str]], semester: int | None) -> list[Student] | int:
    passed = []
    count = 0
    for student in course:
        info, grade = student
        uco, name, sem = info
        if semester is not None:
            if grade != "F" and sem == semester:
                passed.append(info)
                count += 1
        else:
            if grade != "F":
                count += 1
    return count

# ‹student_grade› returns grade with id number ‹uco›.
# if there is no such student, return ‹None›.

def student_grade(uco: int, course: list[tuple[Student, str]]) -> str | None:
    for student in course:
        info, grade = student
        ids, name, sem = info
        if uco == ids:
            return grade
    return None

def main() -> None:
    s1 = (311799, "Dennis Ritchie", 1)
    s2 = (121436, "George Boole", 3)
    s3 = (463522, "Ada Lovelace", 3)
    s4 = (336100, "Alonzo Church", 2)
    s5 = (378500, "Noam Chomsky", 1)
    s6 = (473521, "Donald Knuth", 1)

    ib111 = [(s1, "F"), (s2, "A"), (s4, "E"), (s6, "F")]
    ib001 = [(s2, "D"), (s4, "C"), (s3, "F"), (s5, "D"), (s6, "B")]
    ib002 = [(s6, "A"), (s1, "B"), (s3, "A"), (s4, "C"), (s5, "A")]

    failed_ib111 = failed(ib111)
    failed_ib001 = failed(ib001)

    # Test failed
    assert failed_ib111 == [s1, s6] or failed_ib111 == [s6, s1]
    assert failed_ib001 == [s3]
    assert failed(ib002) == []

    # Test count_passed
    assert count_passed(ib111, None) == 2
    assert count_passed(ib001, None) == 4
    assert count_passed(ib002, None) == 5
    assert count_passed(ib002, 1) == 3
    assert count_passed(ib001, 3) == 1
    assert count_passed(ib111, 3) == 1

    # Test student_grade
    assert student_grade(311799, ib111) == "F"
    assert student_grade(311799, ib001) is None
    assert student_grade(311799, ib002) == "B"
    assert student_grade(463522, ib111) is None
    assert student_grade(463522, ib001) == "F"
    assert student_grade(463522, ib002) == "A"
    assert student_grade(473521, ib111) == "F"
    assert student_grade(473521, ib001) == "B"


if __name__ == "__main__":
    main()
