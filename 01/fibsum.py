from ib111 import week_01  # noqa

# Function calculates sum of fibonacci sequence with elements on even indexes. 
# Example ‹fibsum(3) = 44 = 2 + 8 + 34›.

def fibsum(n):
    a = 0
    b = 1
    sumNum = 0
    while 0 < n:
        c = a + b
        a = b
        b = c
        if c % 2 == 0:
            sumNum += c
            n -= 1
    return sumNum

def main():
    assert fibsum(0) == 0
    assert fibsum(1) == 2
    assert fibsum(2) == 10
    assert fibsum(3) == 44
    assert fibsum(4) == 188
    assert fibsum(5) == 798
    assert fibsum(10) == 1089154


if __name__ == "__main__":
    main()
