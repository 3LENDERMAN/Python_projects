from ib111 import week_04  # noqa
from math import sqrt

# ‹distance› calculates distance between ‹a› and ‹b›.
Tp = tuple[float, float, str]
Point = list[tuple[float, float, str]]

def distance(a: Tp, b: Tp) -> float:
    a_x, a_y, _ = a
    b_x, b_y, _ = b
    return sqrt((a_x - b_x) ** 2 + (a_y - b_y) ** 2)


# ‹leftmost_colour› finds color of "leftmost" point
def leftmost_colour(points: Point) -> str:
    x_min, _, result = points[0]

    for x, _, colour in points:
        if x < x_min:
            x_min = x
            result = colour

    return result

# ‹center_of_gravity› gets ‹points› and ‹colour›; returns point in the middle of the space
def center_of_gravity(points: Point, colour: str) -> Tp:
    total_x = 0.0
    total_y = 0.0
    count = 0
    for p_x, p_y, p_colour in points:
        if colour == p_colour:
            total_x += p_x
            total_y += p_y
            count += 1

    return (total_x / count, total_y / count, colour)

# ‹average_nonmatching_distance›, calculates averagfe distance of two colors. Vstupní
def average_nonmatching_distance(points: Point) -> float:
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


def main():
    test_distance()
    test_leftmost_color()
    test_center_of_gravity()
    test_average_nonmatching_distance()


def test_average_nonmatching_distance():
    r00 = (0.0, 0.0, "red")
    r10 = (1.0, 0.0, "red")
    b20 = (2.0, 0.0, "blue")
    b10 = (1.0, 0.0, "blue")
    g30 = (3.0, 0.0, "green")
    y20 = (2.0, 0.0, "yellow")
    w40 = (4.0, 0.0, "white")
    dist = average_nonmatching_distance

    assert dist([r00, b20]) == 2.0
    assert dist([b10, r00, b20]) == 1.5
    assert dist([r00, b20, b10, g30]) == 1.8
    assert dist([r00, b20, g30]) == 2.0
    assert dist([r00, b20, b10, r10]) == 1.0
    assert dist([r00, b10, g30, y20, w40]) == 2.0


def test_center_of_gravity():
    r00 = (0.0, 0.0, "red")
    r22 = (2.0, 2.0, "red")
    b20 = (2.0, 0.0, "blue")
    b02 = (0.0, 2.0, "blue")
    cog = center_of_gravity

    assert cog([r00], "red") == (0.0, 0.0, "red")
    assert cog([r00, r22], "red") == (1.0, 1.0, "red")
    assert cog([b20, b02], "blue") == (1.0, 1.0, "blue")
    assert cog([r00, b02, b20, r22], "red") == (1.0, 1.0, "red")
    assert cog([r00, b02, b20, r22], "blue") == (1.0, 1.0, "blue")

    g68 = (6.0, 8.0, "green")
    g00 = (0.0, 0.0, "green")
    g64 = (6.0, 4.0, "green")
    g86 = (8.0, 6.0, "green")

    assert cog([g68, g00, g64], "green") == (4.0, 4.0, "green")
    assert cog([g68, g00, g64, g86], "green") == (5.0, 4.5, "green")
    assert cog([r22, b20, g68, g00, g64, g86], "green") == (5.0, 4.5, "green")


def test_leftmost_color():
    p1 = (0.0, 0.0, "white")
    p2 = (-2.0, 15.0, "red")
    p3 = (13.0, -15.0, "yellow")
    p4 = (0.0, 1.0, "black")

    assert leftmost_colour([p1]) == "white"
    assert leftmost_colour([p3]) == "yellow"
    assert leftmost_colour([p1, p3]) == "white"
    assert leftmost_colour([p1, p3, p4, p2]) == "red"
    assert leftmost_colour([p1, p4]) == "white"
    assert leftmost_colour([p3, p4]) == "black"


def test_distance():
    p1 = (0.0, 0.0, "white")
    p2 = (1.0, 0.0, "red")

    assert distance(p1, (0.0, -1.0, "red")) == 1.0
    assert distance(p2, p1) == 1.0
    assert distance(p1, p2) == 1.0
    assert distance(p1, (2.0, 0.0, "black")) == 2.0
    assert distance(p1, (3.0, 4.0, "black")) == 5.0
    assert distance((-3.0, -4.0, "black"), p1) == 5.0


if __name__ == '__main__':
    main()  
