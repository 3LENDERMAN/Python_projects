from ib111 import week_03  # noqa

# Function returns cartesian product of two lists -> returns list of tuples.

def cartesian(x, y):
    cart_list = []
    for i in x:
        for j in y:
            cart_list.append((i, j))
    return cart_list

def main():
    assert cartesian([1], [2, 1]) == [(1, 2), (1, 1)]
    assert cartesian([6, 5, 1], [3, 2]) \
        == [(6, 3), (6, 2), (5, 3), (5, 2), (1, 3), (1, 2)]
    assert cartesian([], [1, 2, 3]) == []
    assert cartesian([1, 4], []) == []
    assert cartesian([10, 2, 4], [11, 21, -9]) \
        == [(10, 11), (10, 21), (10, -9), (2, 11), (2, 21), (2, -9),
            (4, 11), (4, 21), (4, -9)]


if __name__ == "__main__":
    main()
