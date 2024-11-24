from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, done, speed, delay


# This procedure draws simple diamond by repeatingly drawing same 
# polygons with slightly different angle, making it look like diamond drawing

def diamond(sides, length):
    angle = 360.0 / sides
    for x in range(sides):
        left(angle)
        polygon(sides,length,angle)
    
def polygon(sides, length, angle):
    for i in range(sides):
        forward(length)
        left(angle)

def main():
    speed(1)
    delay(0)
    diamond(12, 30)
    done()


if __name__ == "__main__":
    main()
