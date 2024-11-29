from ib111 import week_03  # noqa
from math import isclose

# Function takes a list of points in a plane and returns the length of the polyline that passes 
# through these points (i.e. the line that connects every two points in the list with a line segment). 
# Consider both the coordinates and lengths with floating-point numbers (type ‹float›).

# For ‹[(0, 0), (1, 0), (1, 1), (2, 1)]› gives:
#
#       (1, 1) ┌───▶(2, 1)
#              │
#    (0, 0)╶───┘(1, 0)
#
# three segments of length 1. so total length is 3.

def point_distance(a, b):
    ax, ay = a
    bx, by = b
    return ((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5

def length(points):
    length = 0.0
    for path in range(len(points) - 1):
        length += point_distance(points[path], points[path + 1])
    return length

def main(): # run tests
    assert isclose(point_distance((0.0, 0.0), (1.0, 0.0)), 1.0)
    assert isclose(point_distance((3.0, 0.0), (0.0, 4.0)), 5.0)
    assert isclose(length([(0.0, 1.0), (1.0, 1.0), (1.0, 2.0)]), 2.0)
    assert isclose(length([(0.0, 0.0)]), 0.0)
    assert isclose(length([]), 0.0)
    assert isclose(length([(3.0, 5.0), (3.0, 15.0), (4.0, 15.0),
                           (4.0, 0.0), (0.0, 0.0)]), 30.0)
    assert isclose(length([(0.0, 0.0), (3.0, 4.0)]), 5.0)
    assert isclose(length([(0.0, 0.0), (3.0, 4.0), (3.0, 7.0)]), 8.0)


if __name__ == "__main__":
    main()
