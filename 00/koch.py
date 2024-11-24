from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, penup, \
    pendown, done, speed, delay

# Drawing of famous koch curve without using recursion

def koch_snowflake(size, depth):
    for i in range(3):
        pattern(size,depth)
        right(120)

def pattern(size,depth):
    if depth == 0:
        forward(size)
    else:
        size / 3.0
        pattern(size, depth - 1)
        left(60)
        pattern(size, depth - 1)
        right(120)
        pattern(size, depth - 1)
        left(60)
        pattern(size, depth - 1)
        
def main():
    speed(1)
    delay(0)

    koch_snowflake(10, 5)
    done()


if __name__ == "__main__":
    main()
