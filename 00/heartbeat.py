from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, done, speed

# Procedure draws EKG heartbeats, the number of iterations and their amplitude 
# is fully customizable through parameters of the procedure

def heartbeat(amplitude, period, iterations):
    for i in range(iterations):
        if i % period == 0:
            single_beat(amplitude / 2.0)
        else:
            single_beat(amplitude)
    
def single_beat(size):
    forward(20)
    left(80)
    forward(size)
    right(160)
    forward(size*2)
    left(160)
    forward(size)
    right(80)
    forward(20)

def main():
    speed(4)
    heartbeat(30, 3, 5)
    done()


if __name__ == "__main__":
    main()
