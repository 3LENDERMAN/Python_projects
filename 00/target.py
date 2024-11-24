from ib111 import week_00  # noqa
from turtle import forward, left, done, penup, pendown, speed, delay
from math import pi

# Similiar to tunnel, but draws more polygons into each other.

def target(radius, count):
    dist = radius / float(count)
    for i in range(count):
        left(270)
        circle(radius,dist)
        radius -= dist
        
def circle(radius,dist):
    length = (6.28 * radius) / 100
    for i in range(100):
        forward(length)
        left(3.6)
    left(90)
    penup()
    forward(dist)
    pendown()

def main():
    speed(0)
    delay(0)
    target(100, 4)
    done()


if __name__ == "__main__":
    main()
