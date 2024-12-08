from ib111 import week_06  # noqa


# Clear function, which receives a cross-section of the landscape as input and
# calculates how much water will be retained in the given landscape if it rains on it
# indefinitely. The landscape is represented by a sequence of
# non-negative integers, where each represents the height of one section.
# All sections are equally wide and outside the described section of the landscape,
# the height is 0 everywhere.
#
# For example, the landscape ‹[3, 1, 2, 3, 2]› can retain 3 units of water
# (between the first and fourth segments):
#
#   ┌───┐       ┌───┐
#   │   │       │   │
#   │   │   ┌───┤   ├───┐
#   │   │   │   │   │   │
#   │   ├───┤   │   │   │
#   │   │   │   │   │   │
#   └───┴───┴───┴───┴───┘
#     3   1   2   3   2

def lakes(land: list[int]) -> int:
    if len(land) < 3: return 0
    water = 0
    copied = land.copy()
    for slope in range(3, len(land) + 1):
        for x in range(len(land) - slope + 1):
            temp = copied.copy()
            min_barrier = min(copied[x], copied[slope + x - 1])
            sum_slope = 0
            valid = True
            for y in range(x + 1, slope + x - 1): 
                if copied[y] < min_barrier:
                    sum_slope += min_barrier - copied[y]
                    temp[y] += min_barrier - copied[y]
                else: valid = False
            if valid:
                water += sum_slope
                copied = temp
    return water

def main() -> None: # simple tests
    land = [0, 0, 0]
    assert lakes(land) == 0
    assert land == [0, 0, 0]

    assert lakes([20, 0, 1]) == 1
    assert lakes([1, 2, 3, 2, 1]) == 0
    assert lakes([3, 1, 2, 3, 2]) == 3
    assert lakes([2, 0, 1, 3, 2]) == 3
    assert lakes([4, 3, 2, 1, 0, 4]) == 10
    assert lakes([5, 6, 0, 3, 2, 5, 4, 1, 4, 2, 1, 3]) == 16

    land = [4, 3, 2, 3, 1, 4, 5, 5, 3, 2, 1, 3]
    assert lakes(land) == 10
    assert land == [4, 3, 2, 3, 1, 4, 5, 5, 3, 2, 1, 3]


if __name__ == '__main__':
    main()
