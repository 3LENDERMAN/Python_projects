from ib111 import week_03  # noqa


# game «2048» -> Unlike the original game, we will only consider a one-dimensional game plan,ie one line.
#
# Game planis a list of non-negative integers; zeros will represent blanks.
# For example, the list ‹[2, 0, 0, 2, 4, 8, 0]› represents the following situation:
#  ┌───┬───┬───┬───┬───┬───┬───┐
#  │ 2 │   │   │ 2 │ 4 │ 8 │   │
#  └───┴───┴───┴───┴───┴───┴───┘
#
# The basic step of the game is to move left or right. When moving, all
# the numbers will "fall" in the specified direction, with pairs of identical digits added together.
# Thus, scrolling to the left changes the given list to ‹[4, 4, 8, 0, 0, 0, 0]›.

# ‹slide› procedure that will slide the line represented
# by the ‹row› list, either to the left or right. Procedure directly
# modifies the ‹row› parameter and returns ‹True› if a shift occurred
# change; otherwise it returns ‹False›.

def slide(row, to_left) -> bool:
    if row == []: return False
    changed = False
    x = -1; start = (len(row) - 1); end = 0
    if to_left: x = 1; start = 0; end = (len(row) - 1) 
    for i in range(start, end, x):
        val = row[i]
        if val != 0:
            for j in range(i + x, end, x):
                if val == row[j]:
                    row[i] = val * 2
                    row[j] = 0
                    changed = True
                    break
                elif row[j] != 0:
                    break
    remove_zeros(row, to_left)
    return changed

def remove_zeros(row: list[int], to_left: bool) -> None:
    change = True
    x = -1; start = (len(row) - 1); end = 0
    if to_left: x = 1; start = 0; end = (len(row) - 1) 
    while change:
        temp = row.copy()
        for i in range(start, end, x):
            if row[i] == 0 and row[i + x] != 0:
                row[i] = row[i + x]
                row[i + x] = 0 
        if temp == row: change = False

def main():
    row = [0, 2, 2, 0]
    assert slide(row, True)
    assert row == [4, 0, 0, 0]

    row = [2, 2, 2, 2, 2]
    assert slide(row, False)
    assert row == [0, 0, 2, 4, 4]

    row = [2, 0, 0, 2, 4, 2, 2, 2]
    assert slide(row, True)
    assert row == [4, 4, 4, 2, 0, 0, 0, 0]

    row = [3, 0, 6, 3, 3, 3, 6, 0, 6]

    assert slide(row, False)
    assert row == [0, 0, 0, 0, 3, 6, 3, 6, 12]

    row = [16, 8, 4, 2, 0, 0, 0]
    assert not slide(row, True)
    assert row == [16, 8, 4, 2, 0, 0, 0]


if __name__ == '__main__':
    main()
