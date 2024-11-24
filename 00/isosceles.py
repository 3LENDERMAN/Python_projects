from ib111 import week_00  # noqa
from turtle import forward, left, penup, pendown, done, \
    setheading, speed
from math import sqrt, radians, tan

def isosceles(base, angle):
    half_base = float(base) / 2

    height = half_base * tan(radians(angle))

    side = sqrt(height ** 2 + half_base ** 2)
    forward(base)
    left(180 - angle)
    forward(side)
    left(2 * angle)
    forward(side)

def main():  # demo
    speed(5)
    isosceles(100, 45)

    penup()
    setheading(0)
    forward(150)
    pendown()

    isosceles(120, 65)
    done()


if __name__ == "__main__":
    main()
