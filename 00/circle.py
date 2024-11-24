from ib111 import week_00  # noqa
from turtle import speed, delay, forward, backward, left, \
    right, penup, pendown, done

# Drawing of the 3 circles 

def circle(radius):
    penup()
    length = (6.28 * radius) / 100
    forward(radius)
    left(90)
    pendown()
    for i in range(100):
        forward(length)
        left(3.6)
    penup()
    left(90)
    forward(radius)
    

def main():
    speed(0)
    delay(0)

    circle(90)
    penup()
    forward(90)
    pendown()

    circle(60)
    penup()
    forward(210)
    pendown()

    circle(30)
    done()


if __name__ == "__main__":
    main()
