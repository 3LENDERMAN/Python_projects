from ib111 import week_02  # noqa
from math import factorial


# Consider combination numbers, defined like:
#  ⟦ (n¦k) = n! / (k! ⋅ (n - k)!) ⟧

# where ⟦k ≤ n⟧. Factorial is defined: ⟦ n! = ∏ᵢ₌₁ⁿi ⟧

# That means:
#  ⟦ n! / k! = ∏ᵢ₌₁ⁿ i / ∏ᵢ₌₁ᵏ i = ∏ᵢ₌ₖ₊₁ⁿ i ⟧

def comb_for(n, k):
    # Find smaller from ⟦k⟧ and ⟦n - k⟧ 
    # where ⟦(n¦k) = (n¦n-k)⟧.
    if k < n - k:
        k = n - k

    # Multiply all numbers between ⟦k⟧ and ⟦n⟧ excluding k and including n
    numerator = 1
    for i in range(k + 1, n + 1):
        numerator *= i

    return numerator // factorial(n - k)

# Eqvivalent definition but using ‹while› cycle:
def comb_while(n, k):
    if k < n - k:
        k = n - k

    numerator = 1
    i = k + 1

    while i <= n:
        numerator *= i
        i += 1

    return numerator // factorial(n - k)

def main():  # run tests in cycle
    for n in range(1, 50):
        for k in range(1, n):
            naive = factorial(n) // (factorial(k) * factorial(n - k))
            assert comb_for(n, k) == naive
            assert comb_while(n, k) == naive


if __name__ == '__main__':
    main()
