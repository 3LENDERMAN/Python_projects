from ib111 import week_01  # noqa

# Function finds pythagorean triple ⟦(a, b, c)⟧, where ⟦a⟧, ⟦b⟧ and ⟦c⟧ that ⟦a² + b² = c²⟧
#  1. te triple has biggest possible sum ⟦a + b + c⟧,
#  2. ⟦a⟧, ⟦b⟧ are smaller than ‹max_side›.

def largest_triple(max_side):
    largest_sum = 0

    for a in range(1, max_side):
        for b in range(a + 1, max_side):
            c = (a**2 + b**2) ** 0.5
            if c.is_integer(): 
                c = int(c)
                current_sum = a + b + c
                if current_sum > largest_sum:
                    largest_sum = current_sum

    return largest_sum


def main():
    assert largest_triple(10) == 24
    assert largest_triple(25) == 72
    assert largest_triple(100) == 288
    assert largest_triple(150) == 490
    assert largest_triple(1000) == 3290


if __name__ == "__main__":
    main()
