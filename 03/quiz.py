from ib111 import week_03  # noqa

# ‹mark_points›, calculates total points student got on multiple-choice test. 
# Students solution in ‹solution›, correspond to selected answers 
# The correct answers are in the ‹answers› parameter as a list of pairs.

def mark_points(answers, solution):
    index = 0
    points = 0
    for sol, mark in answers:
        if sol == solution[index]:
            points += mark
        index += 1
    return points

def main(): # run tests
    assert mark_points([(0, 2), (0, 3), (0, 4)], [0, 2, 0]) == 6
    assert mark_points([], []) == 0
    assert mark_points([(1, 1), (2, 1), (0, 1), (2, 1), (4, 1)],
                       [1, 2, 3, 4, 4]) \
        == 3
    assert mark_points([(0, 0), (1, 0), (2, 0)], [4, 3, 1]) == 0
    assert mark_points([(1, 1), (0, 3), (2, 3), (4, 3)], [1, 0, 2, 4]) == 10


if __name__ == "__main__":
    main()
