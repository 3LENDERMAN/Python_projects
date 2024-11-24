from ib111 import week_00  # noqa
from turtle import forward, left, penup, pendown, done, speed

def square(size):
    for i in range(4):
        left(90)
        forward(size)

def main():  # demo
    speed(5)
    square(100)
    
    penup()
    forward(100)
    pendown()

    square(50)

    penup()
    forward(200)
    pendown()

    square(170)

    done()


if __name__ == "__main__":
    main()
