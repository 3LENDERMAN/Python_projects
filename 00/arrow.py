from ib111 import week_00  # noqa
from turtle import forward, left, right, penup, pendown, done, speed, backward
from math import sqrt, tan, radians, atan, cos

# Drawing of arrow with specified dimensions and angle of the tip    

def arrow(width, height, angle):
    base_angle = 90 - (angle / 2.0)    
    arrow_width = (height / 2.0) * tan(radians(base_angle))
    real_width = width - arrow_width
    side = sqrt((arrow_width**2) + ((float(height) / 2) **2))
    
    print(real_width)
    print(width)
    print(arrow_width)
    print(side)
    print(height)
    
    left(90)
    forward(height / 4.0)
    right(90)
    forward(real_width)
    left(90)
    forward(height / 4.0)
    right(180 - base_angle)
    forward(side)
    left(180 + angle)
    forward(side)
    right(180 - base_angle)
    forward(height / 4.0)
    left(90)
    forward(real_width)
    right(90)
    forward(height / 4.0)
    right(90)
        
    
def main():
    speed(5)
    arrow(150, 100, 90)
    penup()
    forward(200)
    pendown()
    arrow(150, 100, 45)
    
    done()


if __name__ == "__main__":
    main()


