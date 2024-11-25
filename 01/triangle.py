from ib111 import week_01  # noqa

# Procedure that checks if triangle with sides (a,b,c) is possible "True" or impossible "False"
def is_triangle(a, b, c):
    return (a + b > c) and (b + c > a) and (c + a > b)

def main():  # demo
    assert is_triangle(3, 4, 5)
    assert is_triangle(1, 1, 1)
    assert not is_triangle(1, 1, 3)
    assert not is_triangle(2, 3, 1)

if __name__ == "__main__":
    main()
