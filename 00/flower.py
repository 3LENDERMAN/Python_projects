from ib111 import week_00  # noqa
from turtle import forward, right, penup, pendown, setheading, \
    done, speed

def triangle():
    forward(100)
    right(165)
    forward(52)
    right(30)
    forward(52)
    right(165)


def flower(petals):
    for i in range(petals):
        if i % 3 != 0 and i % 5 != 0:
            triangle()

        right(360.0 / petals)


def main():  # demo
    speed(10)
    flower(15)

    penup()
    setheading(0)
    forward(220)
    pendown()

    flower(30)
    done()


if __name__ == "__main__":
    main()
