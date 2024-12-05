from ib111 import week_05  # noqa


# "game of life" – a simple two-dimensional cellular automaton. 
# The simulation runs on a square grid, where each cell is dead-0 or alive-1.
# At each step, the value of all cells is recalculated, depending on
# whether they were alive in the previous step and how many live neighbors they had
#
# │ state │ living neigh │  result  │
# ├───────┼──────────────┼──────────┤
# │ alive │          0–1 │    dead  │
# │ alive │          2–3 │    alive │
# │ alive │          4–8 │    dead  │
# │┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄│
# │ dead  │          0–2 │    dead  │
# │ dead  │            3 │    alive │
# │ dead  │          4-8 │    dead  │

# Example:
#
#  ┌───┬───┬───┐   ┌───┬───┬───┐   ┌───┬───┬───┐
#  │   │ ○ │ ○ │   │ ○ │   │ ○ │   │   │ ○ │   │
#  ├───┼───┼───┤   ├───┼───┼───┤   ├───┼───┼───┤
#  │ ○ │ ○ │ ○ │ → │ ○ │   │   │ → │ ○ │   │   │
#  ├───┼───┼───┤   ├───┼───┼───┤   ├───┼───┼───┤
#  │   │ ○ │ ○ │   │ ○ │   │ ○ │   │   │ ○ │   │
#  └───┴───┴───┘   └───┴───┴───┘   └───┴───┴───┘
#
# Different periodical procedure:
#
#  ┌───┬───┬───┐   ┌───┬───┬───┐   ┌───┬───┬───┐
#  │   │   │   │   │   │ ○ │   │   │   │   │   │
#  ├───┼───┼───┤   ├───┼───┼───┤   ├───┼───┼───┤
#  │ ○ │ ○ │ ○ │ → │   │ ○ │   │ → │ ○ │ ○ │ ○ │
#  ├───┼───┼───┤   ├───┼───┼───┤   ├───┼───┼───┤
#  │   │   │   │   │   │ ○ │   │   │   │   │   │
#  └───┴───┴───┘   └───┴───┴───┘   └───┴───┴───┘
#
# Clear function takes state of the game and number of plays and 
# returns state of the game after number of steps in parameter

def count_neighbors(cell: tuple[int, int], cells: set[tuple[int, int]]) -> int:
    x, y = cell
    neighbors = 0
    # Check all 8 possible neighbors around the cell
    for nx in range(x - 1, x + 2):
        for ny in range(y - 1, y + 2):
            if (nx, ny) != (x, y) and (nx, ny) in cells:
                neighbors += 1
    return neighbors

def get_candidates(cells: set[tuple[int, int]]) -> set[tuple[int, int]]:
    # Find all candidate cells to evaluate for the next generation
    candidates = set()
    for x, y in cells:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                candidates.add((x + dx, y + dy))
    return candidates

def next_generation(cells: set[tuple[int, int]]) -> set[tuple[int, int]]:
    candidates = get_candidates(cells)
    new_cells = set()

    # Evaluate each candidate cell to determine if it will be alive in the next generation
    for cell in candidates:
        neighbors = count_neighbors(cell, cells)
        if (cell in cells and neighbors in {2, 3}) or (cell not in cells and neighbors == 3):
            new_cells.add(cell)
    
    return new_cells

def life(cells: set[tuple[int, int]], n: int) -> set[tuple[int, int]]:
    # Run the simulation for n generations
    for _ in range(n):
        cells = next_generation(cells)
    return cells


def lisfe(cells: set[tuple[int, int]], n: int) -> set[tuple[int, int]]:
    if len(cells) <= 1: 
        return set()
    
    # Initialize boundaries
    max_x = -10000000
    min_x = 100000000
    max_y = -10000000
    min_y = 100000000
    for x,y in cells:
        max_x = max(max_x, x)
        min_x = min(min_x, x)
    for x,y in cells:
        max_y = max(max_y, y)
        min_y = min(min_y, y)
    temp_set = cells.copy()

    while n > 0:  # Perform the simulation for n steps
        n -= 1
        change = set()  # This will store the next state
        # Iterate over all relevant coordinates
        for i in range(min_x - 1, max_x + 2):
            for j in range(min_y - 1, max_y + 2):
                neighbors = 0
                # Count living neighbors
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if (k, l) in temp_set and (i, j) != (k, l):
                            neighbors += 1
                # Apply Game of Life rules
                if (i, j) in temp_set:
                    if neighbors == 2 or neighbors == 3:
                        change.add((i, j))  # Stay alive
                else:
                    if neighbors == 3:
                        change.add((i, j))  # Become alive

        temp_set = change  # Update current state

    return temp_set

def lifye(cells: set[tuple[int, int]], n: int) -> set[tuple[int, int]]:
    if len(cells) <= 1: return set()
    max_x = -10000000
    min_x = 100000000
    max_y = -10000000
    min_y = 100000000
    for x,y in cells:
        max_x = max(max_x, x)
        min_x = min(min_x, x)
    for x,y in cells:
        max_y = max(max_y, y)
        min_y = min(min_y, y)
    temp_set = cells.copy()
    change = temp_set.copy()
    while n > 0: # do one step in calculation:
        n -= 1
        for i in range(min(min_x, min_y), max(max_x, max_y) + 1):
            for j in range(min(min_x, min_y), max(max_x, max_y) + 1):
                neighbors = 0
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if (k,l) in temp_set and (i,j) != (k,l):
                            neighbors += 1
                if (i, j) in temp_set:
                    if neighbors < 2 or neighbors > 3: change.remove((i, j))
                    else: continue
                else: 
                    if neighbors == 3: change.add((i, j))                    
        temp_set = change.copy()
    return change


def main() -> None:
    assert life(set(), 3) == set()
    assert life({(0, 0)}, 1) == set()
    block = {(0, 0), (1, 1), (0, 1), (1, 0)}

    blinker_0 = {(0, -1), (0, 0), (0, 1)}
    blinker_1 = {(-1, 0), (0, 0), (1, 0)}
    glider = blinker_1.copy()
    glider.add((1, -1))
    glider.add((0, -2))

    for i in range(20):
        assert life(block, i) == block, life(block, i)

    for i in range(20):
        expect = blinker_0 if i % 2 == 0 else blinker_1
        assert life(blinker_0, i) == expect

    for i in range(0, 40, 4):
        expect = set()
        for x, y in glider:
            expect.add((x + i // 4, y + i // 4))
        assert life(glider, i) == expect, (i, life(glider, i), expect)


if __name__ == "__main__":
    main()
