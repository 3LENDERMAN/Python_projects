from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, penup, \
    pendown, speed, delay, done


# Hilbert curve with depth number of iterations.
def hilbert_curve(size, depth, angle):
    if depth == 0:
        return
    right(angle)
    hilbert_curve(size, depth - 1 , -angle)
    forward(size)
    left(angle)
    hilbert_curve(size, depth - 1 , angle)
    forward(size)
    hilbert_curve(size, depth - 1 , angle)
    left(angle)
    forward(size)
    hilbert_curve(size, depth - 1 , -angle)
    right(angle)
    

def hilbert(size, iterations):
    hilbert_curve(size / (2.0 ** iterations), iterations, 90)
    


def main():
    speed(1)
    delay(0)
    hilbert(100, 1)

    penup()
    forward(20)
    pendown()

    hilbert(100, 2)

    penup()
    forward(20)
    pendown()

    hilbert(100, 3)

    penup()
    forward(20)
    pendown()

    hilbert(100, 4)

    done()


if __name__ == "__main__":
    main()
