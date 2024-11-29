from ib111 import week_03

# Function fib creates a list of first <n> members of fibonacci sequence
def fib(n):
    out = [1, 1]

    for i in range(n - 2):
        value = out[-1] + out[-2]
        out.append(value)

    while len(out) > n:
        out.pop()

    return out

def main():  # run simple tests
    assert fib(0) == []
    assert fib(1) == [1]
    assert fib(2) == [1, 1]
    assert fib(3) == [1, 1, 2]
    assert fib(5) == [1, 1, 2, 3, 5]
    assert fib(9) == [1, 1, 2, 3, 5, 8, 13, 21, 34]

if __name__ == "__main__":
    main()
