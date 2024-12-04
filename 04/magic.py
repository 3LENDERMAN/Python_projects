from ib111 import week_04  # noqa

# A magic square is a two-dimensional matrix of mutually distinct positive integers
# for which the sums of the numbers in each row, each column, and
# both main diagonals are the same. A classic example is the 3x3 magic
# square:
# 8 1 6
# 3 5 7
# 4 9 2
# in which the sums of all rows, all columns, and both diagonals are equal to 15.

# the is_magic_square predicate, which takes a two-dimensional array
# of integers as input and verifies that it is a magic square.


def is_magic_square(square: list[list[int]]) -> bool:
    if square == []:
        return True
    n = sum(square[0])
    cols = len(square[0])
    # check uniqness:
    for i in range(cols):
        for j in range(cols):
            num = square[i][j]
            for k in range(cols):
                for l in range(cols):
                    if square[k][l] == num and k != i and l != j:
                        return False 
    # check rows:   
    for row in square:
        if sum(row) != n: return False
    # check columns:
    for i in range(cols):
        summ = 0
        for row in square:
            summ += row[i]
        if summ != n: return False
    # check diagonals:
    summ = 0
    for x in range(cols):
        summ += square[x][x]
    if summ != n: return False

    return True


def main() -> None:
    assert is_magic_square([[8, 1, 6], [3, 5, 7], [4, 9, 2]])
    assert is_magic_square([])
    assert is_magic_square([[1]])
    assert not is_magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert not is_magic_square([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    assert is_magic_square([[16, 2, 3, 13], [5, 11, 10, 8],
                           [9, 7, 6, 12], [4, 14, 15, 1]])


if __name__ == "__main__":
    main()
