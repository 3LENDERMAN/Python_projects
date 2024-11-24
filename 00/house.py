from ib111 import week_00  # noqa
from turtle import forward, penup, pendown, done, setheading, left, right, backward
from math import sqrt, tan, atan, radians, cos, sin, degrees

# Drawing of the house by one stroke
# Roof angle can have 1 - 179 degrees

def house(width, height, roof_angle):
    angle = 90 - (roof_angle / 2.0)
    triangle_height = (width / 2.0) * tan(radians(angle))
    roof_size = sqrt((width / 2.0)**2 + triangle_height**2)
    side = sqrt(width**2 + height**2)
    house_angle = degrees(atan(float(height) / width))

    forward(width)
    left(180 - angle)
    forward(roof_size)
    left(180 - roof_angle)
    forward(roof_size)
    left(180 - angle)
    forward(width)
    right(90)
    forward(height)
    right(90 + house_angle)
    forward(side)
    left(180 - (90 - house_angle))
    forward(height)
    left(90)
    forward(width)
    backward(width)
    left(house_angle)
    forward(side)
    right(house_angle)
    penup()
    
def main():
    house(150, 100, 75)

    penup()
    setheading(0)
    forward(100)
    pendown()

    house(100, 150, 30)
    done()


if __name__ == "__main__":
    main()
