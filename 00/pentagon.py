from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, penup, pendown, \
    done, speed

# Procedure that draws two simple pentagons with "side" length:

def pentagon(side):
    for i in range(5):
        forward(side)
        left(72)


def main():
    speed(4)
    pentagon(80)

    penup()
    forward(200)
    pendown()

    pentagon(60)
    done()


if __name__ == "__main__":
    main()
