from ib111 import week_00  # noqa
from turtle import forward, left, right, penup, pendown, \
    setheading, done, speed

from math import sqrt, atan, degrees
# Drawing of trapezoid with parameters base, top base and height

def trapezoid(base_length, top_length, height):
    x = (base_length - top_length) / 2.0
    y = sqrt(x**2 + height**2)
    angle = degrees(atan(height / x))
    forward(base_length)
    left(180-angle)
    forward(y)
    left(angle)
    forward(top_length)
    left(angle)
    forward(y)
    left(angle+90)

def main():
    speed(4)
    trapezoid(100, 70, 70)

    penup()
    setheading(0)
    forward(150)
    pendown()

    trapezoid(120, 30, 35)

    done()


if __name__ == "__main__":
    main()
