from ib111 import week_06  # noqa

# Consider simple graph where height of route on ceratin distance 
# is represented by column on graph. We will calculate for how many 
# steps we stayed at height we are currently on (x in example is current pos)
# all the previous height has to be same height or higher.
#
#   ┌─┐     ┌─┐          ┌─┐     ┌─┐          ┌─┐     ┌─┐
#   │░├─┐ ┌─┤ ├─┐ ┌─┐    │░├─┐ ┌─┤ ├─┐ ┌─┐    │░├─┐ ┌─┤ ├─┐ ┌─┐
#   │░│ │ │ │ │ ├─┤ │    │░│░│ │ │ │ ├─┤ │    │░│░│ │ │ │ ├─┤ │
#   │░│ ├─┤ │ │ │ │ ├─┐  │░│░├─┤ │ │ │ │ ├─┐  │░│░├─┤ │ │ │ │ ├─┐
#   │░│ │ │ │ │ │ │ │ │  │░│░│ │ │ │ │ │ │ │  │░│░│░│ │ │ │ │ │ │
#   └─┴─┴─┴─┴─┴─┴─┴─┴─┘  └─┴─┴─┴─┴─┴─┴─┴─┴─┘  └─┴─┴─┴─┴─┴─┴─┴─┴─┘
#    ×                    0 ×                  0   ×
#
#   ┌─┐     ┌─┐          ┌─┐     ┌─┐          ┌─┐     ┌─┐
#   │ ├─┐ ┌─┤ ├─┐ ┌─┐    │ ├─┐ ┌─┤░├─┐ ┌─┐    │ ├─┐ ┌─┤░├─┐ ┌─┐
#   │ │ │ │░│ │ ├─┤ │    │ │ │ │ │░│ ├─┤ │    │ │ │ │░│░│░├─┤ │
#   │ │ ├─┤░│ │ │ │ ├─┐  │ │ ├─┤ │░│ │ │ ├─┐  │ │ ├─┤░│░│░│ │ ├─┐
#   │ │ │ │░│ │ │ │ │ │  │ │ │ │ │░│ │ │ │ │  │ │ │ │░│░│░│ │ │ │
#   └─┴─┴─┴─┴─┴─┴─┴─┴─┘  └─┴─┴─┴─┴─┴─┴─┴─┴─┘  └─┴─┴─┴─┴─┴─┴─┴─┴─┘
#          ×                      ×                  3   ×
#
#   ┌─┐     ┌─┐          ┌─┐     ┌─┐         ┌─┐     ┌─┐
#   │ ├─┐ ┌─┤░├─┐ ┌─┐    │ ├─┐ ┌─┤ ├─┐ ┌─┐   │░├─┐ ┌─┤░├─┐ ┌─┐
#   │ │ │ │░│░│░├─┤ │    │ │ │ │ │ │ ├─┤░│   │░│░│ │░│░│░├─┤░│
#   │ │ ├─┤░│░│░│░│ ├─┐  │ │ ├─┤ │ │ │ │░├─┐ │░│░├─┤░│░│░│░│░├─┐
#   │ │ │ │░│░│░│░│ │ │  │ │ │ │ │ │ │ │░│ │ │░│░│░│░│░│░│░│░│░│
#   └─┴─┴─┴─┴─┴─┴─┴─┴─┘  └─┴─┴─┴─┴─┴─┴─┴─┴─┘ └─┴─┴─┴─┴─┴─┴─┴─┴─┘
#          3     ×                      ×     0               ×

# ‹hills› gets list of heights and which will result in an equally long
# list of indexes that always correspond to the first colored column
# in the illustration above.

def hills(heights: list[int]) -> list[int]:
    # variable stack will act like regular stack: remember last values of heights

    stack: list[int] = []
    indices: list[int] = []
    for i in range(len(heights)):
        while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if len(stack) == 0:
            indices.append(0)
        else:
            indices.append(stack[-1] + 1)
        stack.append(i)
    return indices

def main() -> None:  # tests
    assert hills([1, 2, 3]) == [0, 1, 2]
    assert hills([3, 2, 1]) == [0, 0, 0]
    assert hills([1, 2, 1]) == [0, 1, 0]
    assert hills([2, 2, 2]) == [0, 0, 0]
    assert hills([1, 2, 3, 2]) == [0, 1, 2, 1]
    assert hills([1, 3, 2, 3]) == [0, 1, 1, 3]
    assert hills([3, 1, 3, 2]) == [0, 0, 2, 2]
    example = [4, 3, 1, 3, 4, 3, 2, 3, 1]
    assert hills(example) == [0, 0, 0, 3, 4, 3, 3, 7, 0]


if __name__ == '__main__':
    main()
