from ib111 import week_00  # noqa
from turtle import forward, left, done, speed

def triangle():
    for i in range(3):
        forward(100)
        left(120)

def hexagon():
    for i in range(6):
        triangle()
        left(360.0 / 6)

def main():  # demo
    speed(5)
    hexagon()
    done()


if __name__ == "__main__":
    main()
