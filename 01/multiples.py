from ib111 import week_01  # noqa

# Procedure returns sum of first ⟦aᵢ⟧, where ⟦aᵢ ≤⟧ ‹n› and ⟦3 | aᵢ⟧ or ⟦5 | aᵢ⟧
def sum_of_multiples(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

def main():
    assert sum_of_multiples(10) == 33
    assert sum_of_multiples(13) == 45
    assert sum_of_multiples(14) == 45
    assert sum_of_multiples(16) == 60
    assert sum_of_multiples(100) == 2418
    assert sum_of_multiples(1000) == 234168


if __name__ == "__main__":
    main()
