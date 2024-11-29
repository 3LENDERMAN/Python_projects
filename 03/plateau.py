from ib111 import week_03  # noqa

# "upper plateau" are two or more same numbers besides each other where on the left
# and on the right are values smaller.

# ‹rightmost_plateau› returns index of the first member of the rightmost 
# plateau, else return ‹-1›.

def rightmost_plateau(heights):
    index = -1
    if heights == [] or len(heights) == 1:
        return index
    for i in range(len(heights) - 1): # Iterate through all plateaus:
        end_i = plateau_index(i, heights)
        if end_i > i: # Check for plateau
            # Assign value of right side:
            if i == 0: 
                left = heights[i] - 69
            else: 
                left = heights[i - 1]
            # Assign value of left side:
            if end_i == len(heights) - 1: 
                right = heights[end_i] - 69
            else: 
                right = heights[end_i + 1]
            # Check, if both sides are smaller in value:
            if left < heights[i] and right < heights[end_i]:
                index = i
    return index

def plateau_index(start_i, heights):
    # Return index of last element o plateau:
    while (start_i < len(heights) - 1) and (heights[start_i] == heights[start_i + 1]):
        start_i += 1
    return start_i

# ‹rightmost_plateau([2, 2, 4, 5, 5, 2])› returns ‹3›
# because there is only one plateau of ‹5› index of first plateau digit is 3.

def main() -> None: # run tests
    heights = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    print(rightmost_plateau(heights))
    assert rightmost_plateau(heights) == 6
    assert heights == [1, 1, 1, 2, 2, 2, 3, 3, 3]

    heights = [2, 2, 4, 5, 5, 2]
    assert rightmost_plateau(heights) == 3
    assert heights == [2, 2, 4, 5, 5, 2]

    heights = [2, 2, 3, 3, 4]
    assert rightmost_plateau(heights) == -1

    heights = [7]
    assert rightmost_plateau(heights) == -1

    heights = [9, 9, 9, 9, 9, 0, 0, -9, -9, -9]
    assert rightmost_plateau(heights) == 0

    heights = [2, 1, 1, 1, 1, 1, 1, 2]
    assert rightmost_plateau(heights) == -1


if __name__ == '__main__':
    main()
