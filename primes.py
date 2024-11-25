from ib111 import week_01  # noqa


# Pure ‹nth_smallest_prime_divisor› function that returns the ‹index›th
# the smallest prime number occurring in the prime factorization of the number ‹num›.
# If a prime number occurs more than once in the decomposition, we count all of them
# its occurrences, i.e. e.g. in the number ⟦2 · 2 · 3 · 3 · 3 · 5 = 540⟧ is the third
# smallest prime number 3. 
# If ‹num› has fewer primes than ‹index› in decomposition, the function returns ‹None›.

def nth_smallest_prime_divisor(num, index):
    divisor = 2
    while index > 0:
        if num % divisor == 0:
            num //= divisor
            index -= 1
        else:
            divisor = next_prime(divisor)
        if num == 1 and index > 0:
            return None
    return divisor

def next_prime(number):
    while True:
        number += 1
        if is_prime(number):
            return number

def is_prime(num):
    if num < 2: return False
    for i in range(2, num // 2 + 1):
        if num % i == 0: return False
    return True

def main():
    assert nth_smallest_prime_divisor(20, 1) == 2
    assert nth_smallest_prime_divisor(42350, 2) == 5
    assert nth_smallest_prime_divisor(42350, 3) == 5
    assert nth_smallest_prime_divisor(42350, 4) == 7
    assert nth_smallest_prime_divisor(42350, 7) is None


if __name__ == '__main__':
    main()
