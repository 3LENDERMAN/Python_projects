from ib111 import week_00  # noqa
from turtle import forward, left, right, penup, pendown, \
    setheading, done, delay, speed

# Draws slice of the pizza with specified angle and side
def pizza(side, angle):
    forward(side)
    left(90)
    quality = 120
    x = 360.0 / angle
    length = ((6.28 * side) / quality) / x
    for i in range(quality):
        left(angle / float(quality))
        forward(length)
    left(90)
    forward(side)
    left(180 - angle)
    
def main():
    delay(0)
    speed(1)
    pizza(70, 65)

    penup()
    setheading(0)
    forward(150)
    pendown()

    pizza(100, 25)

    done()


if __name__ == "__main__":
    main()
