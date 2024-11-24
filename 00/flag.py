from ib111 import week_00  # noqa
from turtle import forward, left, right, penup, pendown, done, setheading
from math import sqrt, sin, cos, tan, degrees, atan

# Drawing of czech flag

def flag(width, height, triangle_ratio):
    width_triangle = triangle_ratio * width
    side = sqrt((width_triangle**2) + (height / 2.0) **2)
    angle_right = degrees(sin(float(width_triangle / side)))
    angle_left = (90 - angle_right)

    print(angle_right)
    print(angle_left)
    print(side)

    forward(width)
    right(90)
    forward(height)
    right(90)
    forward(width)
    right(90)
    forward(height)
    right(180 - angle_left)
    forward(side)
    


def main():
    flag(150, 100, 0.5)

    penup()
    setheading(0)
    forward(200)
    right(90)
    forward(125)
    left(90)
    pendown()

    flag(100, 150, 0.3)
    done()


if __name__ == "__main__":
    main()
