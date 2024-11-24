from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, done, speed


# This procedure draws simple fence with "planks", if the
# plank proceeds the length of the fence, it crops.

def fence(length, plank_width, plank_height):
    remaining = length
    while remaining > 0:
        if remaining >= plank_width: 
            draw_plank(plank_width, plank_height)
            remaining -= plank_width
        else:
            draw_plank(remaining, plank_height)
            remaining = 0

def draw_plank(w,h):
    for i in range(2):
        forward(w)
        left(90)
        forward(h)
        left(90)
    forward(w)

def main():
    speed(4)
    fence(140, 40, 100)
    done()


if __name__ == "__main__":
    main()
