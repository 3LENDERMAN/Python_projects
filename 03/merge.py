from ib111 import week_03  # noqa

# (pure) function that creates a new ascendingly sorted list from two ascendingly sorted 
# lists of numbers ‹a›, ‹b›, which will contain all elements from both ‹a› and ‹b›.

def merge(a, b):
    new_list = []
    a_i = len(a)
    b_i = len(b)
    curr_a = 0
    curr_b = 0
    while True:
        if curr_a == a_i and curr_b == b_i:
            return new_list
        if curr_a == a_i:
            new_list.append(b[curr_b])
            curr_b += 1
            continue
        elif curr_b == b_i:
            new_list.append(a[curr_a])
            curr_a += 1
            continue
        if a[curr_a] == b[curr_b]:
            new_list.append(a[curr_a])
            new_list.append(b[curr_b])
            curr_a += 1
            curr_b += 1
        elif a[curr_a] < b[curr_b]:
            new_list.append(a[curr_a])
            curr_a += 1
        elif a[curr_a] > b[curr_b]:
            new_list.append(b[curr_b])
            curr_b += 1


def main(): # run tests
    assert merge([1, 2, 3], [1, 2, 3]) == [1, 1, 2, 2, 3, 3]
    assert merge([0, 2, 4, 6, 8], [1, 3, 5, 7, 9]) \
        == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert merge([], []) == []
    assert merge([], [1, 2]) == [1, 2]
    assert merge([1, 2], []) == [1, 2]
    assert merge([1, 5, 10], [-1, 2, 3, 4, 6, 10, 11]) \
        == [-1, 1, 2, 3, 4, 5, 6, 10, 10, 11]


if __name__ == "__main__":
    main()
