from ib111 import week_01  # noqa


# Clean function ‹largest_on_path› that returns the largest
# the number we encounter if:
#
# • if ‹num› is even, we divide it by two,
# • if ‹num› is odd and greater than 1, we multiply it by three and_add 1,
# • if ‹num› is equal to one, we are done.

def largest_on_path(num):
    largest = num
    while num != 1:
        if num % 2 == 0:
            num //= 2
        elif num % 2 != 0:
            num = num * 3 + 1
        if largest < num:
            largest = num

    return largest

def main():
    assert largest_on_path(1) == 1
    assert largest_on_path(19) == 88
    assert largest_on_path(20) == 20
    assert largest_on_path(27) == 9232


if __name__ == '__main__':
    main()
