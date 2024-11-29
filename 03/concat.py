from ib111 import week_03  # noqa

# Function that joins lists together into one.

def concat(lists):
    new_list = []
    for lst in lists:
        for i in range(len(lst)):
            new_list.append(lst[i])
    return new_list

def main(): # run tests
    assert concat([[1], [2], [1, 2]]) == [1, 2, 1, 2]
    assert concat([[0, 40, 1], [43, -1], [2]]) == [0, 40, 1, 43, -1, 2]
    assert concat([[1]]) == [1]
    assert concat([[], [1], []]) == [1]
    assert concat([[1, 1, 1], [1], [1, 1]]) == [1, 1, 1, 1, 1, 1]


if __name__ == "__main__":
    main()
