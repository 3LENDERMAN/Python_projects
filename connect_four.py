from ib111 import week_05  # noqa

# «Connect Four» simple two player game where each player places either circle or cross
# the symbol "falls" on upper or empty box and first player to have 4 matching symbols
# either on rows, columns or diagonals, wins.
# Representaion of players is "X" and "O", for example,
# list ‹[['X'], [], ['O', 'X'], [], ['X', 'O', 'O'], [], []]›, represents:
#  ┌───┬───┬───┬───┬───┬───┬───┐
#  │   │   │   │   │ O │   │   │
#  ├───┼───┼───┼───┼───┼───┼───┤
#  │   │   │ X │   │ O │   │   │
#  ├───┼───┼───┼───┼───┼───┼───┤
#  │ X │   │ O │   │ X │   │   │
#  └───┴───┴───┴───┴───┴───┴───┘
#    0   1   2   3   4   5   6
# There is no upper limit so there can be unlimited number of rows
#
# For playing grid, we have type alias ‹Grid›.

Grid = list[list[str]]

# Function <to_matrix> converts list to matrix consisted of strings with empty spaces
# For previously mentioned grid, ‹to_matrix› returns:
# ‹[[" ", " ", " ", " ", "O", " ", " "],
#   [" ", " ", "X", " ", "O", " ", " "],
#   ["X", " ", "O", " ", "X", " ", " "]]›

def to_matrix(grid: Grid) -> list[list[str]]:
    temp = 0
    highest = 0
    playground: list[list[str]] = []
    for col in grid:
        if len(col) > highest:
            highest = len(col)
    for i in range(highest - 1, -1, -1):
        row: list[str] = []
        for col in grid:
            if (len(col) - 1) >= i:
                row.append(col[i])
            else:
                row.append(" ")
        playground.append(row)
    return playground

# Procedure ‹play› returns if after play of <player> on column <column> 
# will one of the players win (consider there is no winner so far).

def play(grid: Grid, player: str, column: int) -> bool:
    grid[column].append(player)
    index = (len(grid[column]) - 1)
    return is_winner(grid, index, column)

# Function <is_winner> checks all valid possibilities from simplest to most complicated and returns 
# final boolean value to function <play>:

def is_winner(grid: Grid, index: int, column: int) -> bool:
    # check if there is a match on the columns:
    for col in grid:
        if len(col) > 3:
            if col[len(col) - 1] == col[len(col) - 2] == col[len(col) - 3] == col[len(col) - 4]:
                return True
    # check if there is a match on the rows:
    if len(grid) > 3:
        for j in range(len(grid) - 3):
            if len(grid[j]) - 1 >= index and len(grid[j + 1]) - 1 >= index and len(grid[j + 2]) - 1 >= index and len(grid[j + 3]) - 1 >= index:
                if grid[j][index] == grid[j + 1][index] == grid[j + 2][index] == grid[j + 3][index]:
                    return True
    # check if there is a match on the diagonals:
    if len(grid[column + 1]) >= index and len(grid) - 1 >= column + 3: 
        if len(grid[column + 1]) - 1 >= index - 1 and len(grid[column + 2]) - 1 >= index - 2 and len(grid[column + 3]) - 1 >= index - 3:
            if grid[column][index] == grid[column + 1][index - 1] == grid[column + 2][index - 2] == grid[column + 3][index - 3]:
                return True

    if column >= 3 and index >= 3:
        if len(grid[column]) > index and len(grid[column - 1]) - 1 >= index - 1 and len(grid[column - 2]) - 1 >= index - 2 and len(grid[column - 3]) - 1 >= index - 3:
            if grid[column][index] == grid[column - 1][index - 1] == grid[column - 2][index - 2] == grid[column - 3][index - 3]:
                return True
    return False

def main() -> None: # Run simple tests..
    grid: Grid = [['X'], [], ['O', 'X'], [], ['X', 'O', 'O'], [], []]
    assert to_matrix(grid) == [
        [" ", " ", " ", " ", "O", " ", " "],
        [" ", " ", "X", " ", "O", " ", " "],
        ["X", " ", "O", " ", "X", " ", " "],
    ]

    assert not play(grid, 'X', 3)
    assert grid == [['X'], [], ['O', 'X'], ['X'], ['X', 'O', 'O'], [], []]

    assert not play(grid, 'O', 3)
    assert grid == [['X'], [], ['O', 'X'], ['X', 'O'], ['X', 'O', 'O'], [], []]

    assert not play(grid, 'X', 5)
    assert grid \
        == [['X'], [], ['O', 'X'], ['X', 'O'], ['X', 'O', 'O'], ['X'], []]

    assert not play(grid, 'O', 5)
    assert grid \
        == [['X'], [], ['O', 'X'], ['X', 'O'], ['X', 'O', 'O'], ['X', 'O'], []]

    assert not play(grid, 'X', 5)
    assert grid \
        == [['X'], [], ['O', 'X'], ['X', 'O'],
            ['X', 'O', 'O'], ['X', 'O', 'X'], []]

    assert play(grid, 'O', 5)
    assert grid \
        == [['X'], [], ['O', 'X'], ['X', 'O'],
            ['X', 'O', 'O'], ['X', 'O', 'X', 'O'], []]


if __name__ == '__main__':
    main()
