from ib111 import week_03  # noqa


# Consider list of 2D plateaus represented by numbers
# Plateau is when two or more same values are beside each other

# ‹flats› returns all plateaus each represented by theirs heights

def flats(heights):
    new_list = []
    val = -1000
    if heights == []:
        return []
    for i in range(len(heights) - 1):
        if heights[i] == heights[i + 1] and val != heights[i]:
            new_list.append(heights[i])
        val = heights[i]
    return new_list

# Examples:
# ‹flats([2, 2, 4, 5, 4, 4, 3])› returns ‹[2, 4]›.
# ‹flats([1, 2, 2, 10, 2, 9, 3, 3, 2, 2])› returns ‹[2, 3, 2]›.

def main() -> None: # run tests
    heights = [2, 2, 2, 2, 4, 5, 4, 4, 3]
    assert flats(heights) == [2, 4]
    assert heights == [2, 2, 2, 2, 4, 5, 4, 4, 3]

    heights = [1, 2, 3, 5, 4, 7, 2, 1]
    assert flats(heights) == []

    heights = [1, 2, 2, 10, 2, 9, 3, 3, 2, 2]
    assert flats(heights) == [2, 3, 2]

    heights = [0, 0, 1, 1, 2, 2, 0, 2, 2, 0, 2]
    assert flats(heights) == [0, 1, 2, 2]
    assert heights == [0, 0, 1, 1, 2, 2, 0, 2, 2, 0, 2]

    heights = []
    assert flats(heights) == []


if __name__ == '__main__':
    main()
