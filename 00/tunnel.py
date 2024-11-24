from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, done, \
    penup, pendown, speed

# Draws tunnel by making smaller and smaller squares embbeded 
# into each other 

def tunnel(size, step):
    while size >= 0:
        square(size)
        start(step)
        size -= step
                
def square(size):
    for i in range(4):
        forward(size)
        left(90)

def start(dist):
    left(45)
    penup()
    forward(dist*0.75)###
    right(45)
    pendown()

def main():
    speed(5)
    tunnel(150, 30)
    done()


if __name__ == "__main__":
    main()
