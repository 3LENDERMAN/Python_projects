from ib111 import week_03  # noqa

# ‹largest_exponent› takes a list of numbers and returns the ones that are 
# the largest powers of the given prime number in the prime factorization of
# the given prime number. If there are multiple numbers with the same powers of
# prime num in the factorization, it returns the smallest. [24, 36, 54], 2

def largest_exponent(numbers, prime):
    in_list = numbers[0]
    largest = 0
    index = 0
    for number in numbers:
        exponent = 0
        prime_num = 2
        while number > 1:
            if is_prime(prime_num) and number % prime_num == 0:
                number //= prime_num
                if prime_num == prime:
                    exponent += 1
            else:
                prime_num += 1
        if exponent >= largest:
            if exponent == largest:
                in_list = min(numbers[index], in_list)
            else:
                in_list = numbers[index]
            largest = exponent
        index += 1
    return in_list

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0 and num != i:
            return False
    return True

# Examples:
# ‹largest_exponent([24, 36, 54], 2)› returns ‹24›.
# ‹largest_exponent([625, 1375, 1250], 5)› returns ‹625›.

def main() -> None:
    assert largest_exponent([24, 36, 54], 2) == 24
    assert largest_exponent([625, 1375, 1250], 5) == 625
    assert largest_exponent([2 ** 20, 2 ** 17, 2 ** 17 * 9], 2) == 2 ** 20
    assert largest_exponent([1029, 1225, 1715, 1323, 686], 7) == 686


if __name__ == '__main__':
    main()
