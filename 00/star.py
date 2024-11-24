from ib111 import week_00  # noqa
from turtle import forward, penup, pendown, done, setheading, left, right
from math import radians, tan

# Drawing of the star, initially turtle starts at the "north "tip of the star
# Each tip has angle and size specified 

def draw_triangle(angle, size):
    side = size * tan(radians(angle/ 2.0))
    real_angle = 90 - (angle / 2.0)
    left(real_angle)
    forward(side)
    right(180 - angle)
    forward(side)
    left(real_angle)


def star(points, angle, size):
    side_angle = 360.0 / points
    left(side_angle)
    for i in range(points):
        right(side_angle)
        draw_triangle(angle, size)


def main():
    star(5, 72, 50)

    penup()
    setheading(0)
    forward(200)
    pendown()

    star(6, 30, 50)
    done()


if __name__ == "__main__":
    main()
