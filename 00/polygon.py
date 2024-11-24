from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, penup, pendown, done

# Procedure that draws polygon with "sid" sides and "len" length

def polygon(sid, len):
    angle = 360.0 / sid
    for i in range(sid):
        forward(len)
        right(angle)

def main():
    polygon(7, 40)

    penup()
    forward(120)
    pendown()

    polygon(6, 60)

    penup()
    forward(100)
    pendown()

    polygon(3, 80)

    done()


if __name__ == "__main__":
    main()
