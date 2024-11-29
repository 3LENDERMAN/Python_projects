from ib111 import week_03
from math import sqrt

# (pure) function calculates the Euclidean distance between two points.

def distance(a, b):
    a_x, a_y, _ = a
    b_x, b_y, _ = b
    return sqrt((a_x - b_x) ** 2 + (a_y - b_y) ** 2)


# This function finds value of leftmost color:
def leftmost_colour(points):
    x_min, _, result = points[0]

    for x, _, colour in points:
        if x < x_min:
            x_min = x
            result = colour

    return result

# the parameters will be: a list of points ‹points› and a color ‹colour›, and its result will be a point,
# which is located in the "center of gravity" of the system of points of the given color (the same color).
# The input condition is that ‹points› contains at least one point of color ‹colour›.

def center_of_gravity(points, colour):
    total_x = 0.0
    total_y = 0.0
    count = 0
    for p_x, p_y, p_colour in points:
        if colour == p_colour:
            total_x += p_x
            total_y += p_y
            count += 1

    return (total_x / count, total_y / count, colour)

# The function calculates the average distance between points of different colors.
def average_nonmatching_distance(points):
    total = 0.0
    pairs = 0

    for i in range(len(points)):
        for j in range(i):
            _, _, i_colour = points[i]
            _, _, j_colour = points[j]
            if i_colour != j_colour:
                total += distance(points[i], points[j])
                pairs += 1

    return total / pairs


def main():  # call test functions below
    test_distance()
    test_leftmost_colour()
    test_center_of_gravity()
    test_average_nonmatching_distance()


def test_average_nonmatching_distance():
    r00 = (0, 0, "red")
    r10 = (1, 0, "red")
    b20 = (2, 0, "blue")
    b10 = (1, 0, "blue")
    g30 = (3, 0, "green")
    y20 = (2, 0, "yellow")
    w40 = (4, 0, "white")
    dist = average_nonmatching_distance

    assert dist([r00, b20]) == 2
    assert dist([b10, r00, b20]) == 1.5
    assert dist([r00, b20, b10, g30]) == 1.8
    assert dist([r00, b20, g30]) == 2
    assert dist([r00, b20, b10, r10]) == 1
    assert dist([r00, b10, g30, y20, w40]) == 2


def test_center_of_gravity():
    r00 = (0, 0, "red")
    r22 = (2, 2, "red")
    b20 = (2, 0, "blue")
    b02 = (0, 2, "blue")
    cog = center_of_gravity

    assert cog([r00], "red") == (0, 0, "red")
    assert cog([r00, r22], "red") == (1, 1, "red")
    assert cog([b20, b02], "blue") == (1, 1, "blue")
    assert cog([r00, b02, b20, r22], "red") == (1, 1, "red")
    assert cog([r00, b02, b20, r22], "blue") == (1, 1, "blue")

    g68 = (6, 8, "green")
    g00 = (0, 0, "green")
    g64 = (6, 4, "green")
    g86 = (8, 6, "green")
    green = [g68, g00, g64, g86]

    assert cog([g68, g00, g64], "green") == (4, 4, "green")
    assert cog(green, "green") == (5, 4.5, "green")
    green.append(r22)
    green.append(b20)
    assert cog(green, "green") == (5, 4.5, "green")


def test_leftmost_colour():
    p1 = (0, 0, "white")
    p2 = (-2, 15, "red")
    p3 = (13, -15, "yellow")
    p4 = (0, 1, "black")

    assert leftmost_colour([p1]) == "white"
    assert leftmost_colour([p3]) == "yellow"
    assert leftmost_colour([p1, p3]) == "white"
    assert leftmost_colour([p1, p3, p4, p2]) == "red"
    assert leftmost_colour([p1, p4]) == "white"
    assert leftmost_colour([p3, p4]) == "black"


def test_distance():
    p1 = (0, 0, "white")
    p2 = (1, 0, "red")

    assert distance(p1, (0, -1, "red")) == 1
    assert distance(p2, p1) == 1
    assert distance(p1, p2) == 1
    assert distance(p1, (2, 0, "black")) == 2
    assert distance(p1, (3, 4, "black")) == 5
    assert distance((-3, -4, "black"), p1) == 5


if __name__ == '__main__':
    main()
