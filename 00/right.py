from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, penup, pendown, done

from math import sqrt, atan, radians, degrees
# Implementation of simple procedure that draws right triangle with smaller sides a, b
# and calculated side c 

def right_triangle(side_a, side_b):
    side_c = sqrt(side_a * side_a + side_b * side_b) 
    angle = degrees(atan(float(side_a) / float(side_b)))
    
    forward(side_a)
    left(90+angle)
    forward(side_c)
    left(180-angle)
    forward(side_b)

def main():
    right_triangle(80, 20)

    right(90)
    penup()
    forward(100)
    pendown()
    right(180)

    right_triangle(60, 60)
    done()


if __name__ == "__main__":
    main()
