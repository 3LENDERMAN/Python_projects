from ib111 import week_03  # noqa


# Function ‹survivors› calculates from input list ‹objects› returns all 
# elements from objects list that are far enough from center (further than <radius>)
#
# ‹objects› and ‹center› are triplets which represents vertices in 3D space

def distance(a, b):
    ax, ay, az = a
    bx, by, bz = b

    return ((bx - ax)**2 + (by - ay)**2 + (bz - az)**2) ** 0.5

def survivors(objects, center, radius):
    list_of_survivors = []
    for object in objects:
        if distance(object, center) > radius:
            list_of_survivors.append(object)
    
    return list_of_survivors

def main():
    assert survivors([(1, 0, 0), (2, 1, 1)], (0, 0, 0), 1) \
        == [(2, 1, 1)]
    assert survivors([(3, 2, 3)], (0, 0, 0), 1) == [(3, 2, 3)]
    assert survivors([(1, 1, 1), (0, 0, 1), (2, 0, 0)],
                     (0, 0, 0), 2) \
        == []
    assert survivors([], (0, 0, 0), 25) == []
    assert survivors([(4, 1, 1), (-2, 1, 1), (4, 4, 4)], (1, 1, 1), 3) \
        == [(4, 4, 4)]
    assert survivors([(0, 0, 1), (2, 0, 0), (1, 2, 1), (3, 0, 0)],
                     (1, 0, 1), 2) \
        == [(3, 0, 0)]
    assert survivors([(0, 3, 1), (2, 2, 0), (0, 2, 1), (3, 0, 1)],
                     (1, -2, 1), 4) \
        == [(0, 3, 1), (2, 2, 0), (0, 2, 1)]


if __name__ == "__main__":
    main()
