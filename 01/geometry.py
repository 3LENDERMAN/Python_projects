from ib111 import week_01  # noqa

# Predicate which checks if its possible to create triangle with right angle using ‹a›, ‹b› a ‹c›.
def is_right(a, b, c):
    if c > a and c > b:
        longest = c
    elif b > c and b > a:
        longest = b
        b = c 
        c = longest
    else:
        longest = a
        a = c
        c = longest

    return a**2 + b**2 == c**2

# Checks equilateral triangle:
def is_equilateral(a, b, c):
    return a == b == c

# Checks isosceles triangle:
def is_isosceles(a, b, c):
    if a == b:
        return a > (c // 2)
    elif b == c:
        diff = a
        a = c
        c = diff
    elif a == c:
        diff = b
        b = c
        c = diff
    else:
        return False
    
    return a > (c // 2)
        
def main():
    assert is_right(3, 4, 5)
    assert is_right(4, 3, 5)
    assert is_right(5, 4, 3)
    assert is_right(17, 15, 8)
    assert not is_right(1, 1, 1)
    assert not is_right(2, 5, 5)
    assert not is_right(10, 3, 7)
    assert not is_right(3, 2, 1)

    assert is_equilateral(1, 1, 1)
    assert not is_equilateral(2, 1, 3)

    assert is_isosceles(1, 1, 1)
    assert is_isosceles(2, 2, 1)
    assert is_isosceles(1, 3, 3)
    assert is_isosceles(2, 1, 2)
    assert not is_isosceles(1, 4, 7)
    assert not is_isosceles(3, 1, 7)
    assert not is_isosceles(1, 1, 4)
    assert not is_isosceles(1, 4, 1)
    assert not is_isosceles(4, 1, 1)


if __name__ == "__main__":
    main()
