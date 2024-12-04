from ib111 import week_04  # noqa


# The pure function ‹gambling_score› evaluates the result of a dice roll
# (a non-empty list of integers from 1 to 6 inclusive) as follows:
#
# A triple of the same number is scored as 100 times the rolled number, except for a triple
# of ones, which is scored as 1000. A quadruple of the same number is scored as
# double the value of a triple, a five is scored as double the value of
# a four, etc. If, after counting all triples, fours, fives, etc., there are
# any (yet uncounted) ones and fives left, each one is scored as
# one hundred points, each five is scored as fifty points. The points obtained are added up.
# Example: For input ‹[1, 1, 1, 1, 5, 3, 3, 3, 4]› the function returns ‹2350›
# (four ones for 2000 points, three threes for 300 points, one five for 50).
# For input ‹[2, 2, 5, 2, 2, 5, 2, 2]› the function returns ‹1700›
# (six twos for 1600 points, two fives for 100).
# For input ‹[2, 2, 3, 4, 6, 6]› the function returns ‹0›
# (there is no three or better group of the same numbers, no ones, no fives).
# Note in particular that the order of the numbers in the list does not matter and that we always count
# the maximum number of occurrences of a given number (i.e. after we counted four ones for 2000 points in the first
# example, we no longer consider how many three ones there are in the list).


def gambling_score(dice: list[int]) -> int:
    score = 0
    for i in range(1, 7):
        count = 0
        for digit in dice:
            if digit == i:
                count += 1
        if i == 1 and count > 2:
            score += 1000 * (2 ** (count - 3))
        elif count > 2:
            score += i * 100 * (2 ** (count - 3))
        else:
            if i == 5: score += count * 50
            if i == 1: score += count * 100
    return score


def main() -> None:
    dice = [1, 1, 1, 1, 5, 3, 3, 3, 4]
    assert gambling_score(dice) == 2350
    assert dice == [1, 1, 1, 1, 5, 3, 3, 3, 4]

    assert gambling_score([2, 2, 5, 2, 2, 5, 2, 2]) == 1700
    assert gambling_score([2, 2, 3, 4, 6, 6]) == 0
    assert gambling_score([5, 5, 5, 5, 5]) == 2000
    assert gambling_score([6, 6, 6, 6, 6, 6]) == 4800
    assert gambling_score([1, 2, 3, 4, 5, 6]) == 150
    assert gambling_score([2, 4, 3, 4, 6, 4]) == 400


if __name__ == '__main__':
    main()
