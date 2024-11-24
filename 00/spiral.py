from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, done, speed

# Procedure draws 4-sided spiral from the outer side to the middle

def spiral(rounds, step):
    step = step / 4.0
    for i in range(rounds*4):
        forward(step*i+step)
        right(90)

def main():
    speed(5)
    spiral(5, 50)
    done()


if __name__ == "__main__":
    main()
