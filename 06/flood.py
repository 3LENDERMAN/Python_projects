from ib111 import week_06  # noqa

# «Flood fill» is an algorithm from the field of raster graphics that
# fills a continuous solid-color area with some other color.
# It proceeds by first coloring the position at which
# it starts with a new color, then trying to color its neighbors (positions other than
# the target color are not colored), and similarly continuing with the neighbors of these
# neighbors, etc. It stops when it reaches the edge of the image or encounters
# a pixel that has no new neighbors of the same color.
#
# We consider neighboring pixels only in four directions, i.e. not diagonally.

# The procedure receives an area represented by
# a rectangular list of lists, a starting position (guaranteed to be valid
# coordinates), and a target color to which the selected positions
# are to be recolored.

Position = tuple[int, int]
Area = list[list[int]]

def flood_fill(area: Area, start: Position, colour: int) -> None:
    x, y = start
    original_colour = area[x][y]
    # Use iterative flood fill
    stack = [start]
    while stack:
        cx, cy = stack.pop()
        # If the actual position is as it was and color is the same, assign new color
        if (0 <= cx < len(area) and 0 <= cy < len(area[0]) and area[cx][cy] == original_colour):
            area[cx][cy] = colour
            # Add neighbors to right
            stack.append((cx + 1, cy))  # down
            stack.append((cx - 1, cy))  # up
            stack.append((cx, cy + 1))  # right
            stack.append((cx, cy - 1))  # left

def main() -> None:
    check_flood([[0]], (0, 0), 1, [[1]])
    check_flood([[0, 0, 1, 1, 1, 0]], (0, 3), 2, [[0, 0, 2, 2, 2, 0]])
    check_flood([[0, 0, 1, 1, 1, 0]], (0, 0), 2, [[2, 2, 1, 1, 1, 0]])
    check_flood([[1, 2, 3, 4], [1, 1, 1, 1], [2, 2, 2, 1], [5, 5, 1, 1]],
                (1, 1), 8,
                [[8, 2, 3, 4], [8, 8, 8, 8], [2, 2, 2, 8], [5, 5, 8, 8]])
    check_flood([[1, 2, 3, 4], [1, 1, 1, 1], [2, 2, 2, 1], [1, 5, 1, 1]],
                (1, 1), 8,
                [[8, 2, 3, 4], [8, 8, 8, 8], [2, 2, 2, 8], [1, 5, 8, 8]])


def check_flood(area: Area, start: Position,
                new_colour: int, expected_result: Area) -> None:
    flood_fill(area, start, new_colour)
    assert area == expected_result


if __name__ == '__main__':
    main()
