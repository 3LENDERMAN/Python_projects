from ib111 import week_03  # noqa


# Clear function that gets list of rectangles (their coordinates). 
# And then returns list of rectangles that overlaps with another one.
# Each rectangle is represented by two tuples (coordinate of left bottom and top right point):
# ‹((0, 0), (1, 2))› represents:
#           ┌───┐(1, 2)
#           │   │
#           │   │
#     (0, 0)└───┘


# Predicate that is True when two rectangles overlap:
def has_overlap(a, b):
    (a_x1, a_y1), (a_x2, a_y2) = a 
    (b_x1, b_y1), (b_x2, b_y2) = b 

    if a_x2 <= b_x1 or a_x1 >= b_x2: 
        return False
    if a_y2 <= b_y1 or a_y1 >= b_y2: 
        return False

    return True

def filter_overlapping(rectangles):
    lst = []
    last = None
    if len(rectangles) == 1:
        return []
    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            if has_overlap(rectangles[i], rectangles[j]):
                if rectangles[i] != last:
                    lst.append(rectangles[i])
                    lst.append(rectangles[j])                    
                else: 
                    lst.append(rectangles[j])                    
                last = rectangles[j]
    return lst


def main(): # run tests
    r1 = ((1, 1), (2, 2))
    r2 = ((0, 0), (2, 2))
    r3 = ((-2, -2), (-1, -1))
    r4 = ((10, 15), (25, 35))

    assert filter_overlapping([]) == []
    assert filter_overlapping([r1]) == []
    assert filter_overlapping([r1, r1]) == [r1, r1]
    assert filter_overlapping([r1, r2]) == [r1, r2]
    assert filter_overlapping([r2, r1]) == [r2, r1]

    assert filter_overlapping([r3, r2, r1, r4]) == [r2, r1]
    assert filter_overlapping([r2, ((1, 10), (10, 20))]) == []
    assert filter_overlapping([((15, 0), (17, 8)),
                               ((1, 10), (10, 20))]) == []
    l2 = [((0, 0), (2, 2)),
          ((1, 1), (10, 10)),
          ((9, 9), (11, 11))]
    assert filter_overlapping(l2) == l2


if __name__ == "__main__":
    main()
