from ib111 import week_00  # noqa
from turtle import forward, right, done, penup, pendown, setheading

# Drawing of simple square
def square():
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)

def square_loop():
    for i in range(4):
        forward(100)
        right(90)

def main():  # demo

    square()
    penup()
    setheading(0)
    forward(200)
    pendown()
    square_loop()

    done()


if __name__ == "__main__":
    main()
