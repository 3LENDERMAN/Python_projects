from ib111 import week_04  # noqa
from math import pi, sin, cos, sqrt, isclose

# Exercising type anotations on geometrical shapes:

def disc_area(radius: float) -> float:
    return pi * radius ** 2

Rectangle = tuple[float, float]

def rectangle_area(dimensions: Rectangle) -> float:
    width, height = dimensions
    return width * height

def ellipse_area(semiaxes: tuple[float, float]) -> float:
    major, minor = semiaxes
    return pi * major * minor

def polygon_area(polygon: tuple[float, int]) -> float:
    radius, vertices = polygon
    half_angle = pi / vertices
    half_side = sin(half_angle) * radius
    minor_radius = cos(half_angle) * radius
    return vertices * minor_radius * half_side

Colour = str


def coloured_area(rectangles: list[tuple[Rectangle, Colour]],
                  selected_colour: Colour) -> float:
    area: float = 0

    for rect, colour in rectangles:
        if colour == selected_colour:
            area += rectangle_area(rect)
    return area

def largest_rectangle(rectangles: list[Rectangle]) \
        -> Rectangle | None:

    if len(rectangles) == 0:
        return None

    largest = rectangles[0]
    count = 0

    for r in rectangles:
        if isclose(rectangle_area(r), rectangle_area(largest)):
            count += 1
        elif rectangle_area(r) > rectangle_area(largest):
            count = 1
            largest = r

    return largest if count == 1 else None

def large_rectangles(rectangles: list[Rectangle]) \
        -> list[Rectangle]:
    total = sum([rectangle_area(r) for r in rectangles])
    average = float(total) / len(rectangles)
    result = []
    for r in rectangles:
        if rectangle_area(r) >= average:
            result.append(r)
    return result


def main() -> None:  # run tests
    unit_rectangle = (1, 1)
    assert isclose(rectangle_area(unit_rectangle), 1)
    assert isclose(rectangle_area((2, 2)), 4)
    assert isclose(polygon_area((sqrt(2), 4)), 4)
    assert isclose(polygon_area((1, 6)), 2.5980762113533)
    assert isclose(ellipse_area((1, 1)), 3.1415926535898)
    assert isclose(ellipse_area((2, 6)), 37.699111843078)
    assert isclose(ellipse_area((12.532, 8.4444)), 332.4597362298)

    # assert ellipse_area(unit_rectangle) == 1

    red, green, blue = "red", "green", "blue"
    red_1 = ((1, 1), red)
    red_2 = ((5, 6), red)
    green_1 = ((1, 1), green)
    green_2 = ((5, 6), green)
    blue_1 = ((2, 3), blue)
    assert isclose(coloured_area([red_1, green_1], red), 1)
    assert isclose(coloured_area([red_1, red_2], red), 31)
    assert isclose(coloured_area([red_1, green_2, blue_1], blue), 6)
    assert isclose(coloured_area([red_1, green_1], blue), 0)
    assert largest_rectangle([]) is None
    assert largest_rectangle([(1, 1), (4, 3), (6, 2)]) is None
    assert largest_rectangle([(5, 5), (4, 3), (1, 1)]) == (5, 5)
    assert largest_rectangle([(12, 2), (10.2, 1.5)]) == (12, 2)
    r_1, r_2, r_3 = (1, 3), (5, 5), (7, 2)
    assert large_rectangles([r_1, r_2, r_3]) == [r_2, r_3]
    assert large_rectangles([r_1, r_2]) == [r_2]
    assert large_rectangles([r_1, r_1]) == [r_1, r_1]

if __name__ == '__main__':
    main()