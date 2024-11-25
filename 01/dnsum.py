from ib111 import week_01  # noqa

# Clean function ‹sum_elements_dn› that returns the sum
# of the first ‹count› elements of the ascending positive sequence
# of integers that are both divisible by ‹div› and not
# divisible by ‹nondiv›.

def sum_elements_dn(div, nondiv, count):
    sum = 0
    num = 1
    while count > 0:
        if num % div == 0 and num % nondiv != 0:
            sum += num
            count -= 1

    return sum

def main():
    print(sum_elements_dn(10,6,11))
    assert sum_elements_dn(3, 2, 7) == 147
    assert sum_elements_dn(6, 4, 5) == 150
    assert sum_elements_dn(10, 6, 11) == 910


if __name__ == '__main__':
    main()
