from ib111 import week_03

# This procedure «rotates» a list (in place)
# by the specified number of elements. For example, by rotating the list ‹[1, 2, 3, 4]›:
# • by one to the right we get the list ‹[4, 1, 2, 3]›,
# • by two to the right the list ‹[3, 4, 1, 2]›,
# • by two to the left the same list ‹[3, 4, 1, 2]›,
# • by one to the left the list ‹[2, 3, 4, 1]›.

# Direction of rotation: positive numbers will rotate to the right, negative to the left.

def rotate_naive(lst, amount):
    while amount != 0:
        if amount < 0:
            # Shift left moves the first element to the last place and all others one to the left.
            backup = lst[0]
            for i in range(len(lst) - 1):
                lst[i] = lst[i + 1]
            lst[-1] = backup
            amount += 1
        else:
            # Moving to the right is analogous, but all moves will be in the opposite direction.
            backup = lst[-1]
            for i in range(len(lst) - 1, 0, -1):
                lst[i] = lst[i - 1]
            lst[0] = backup
            amount -= 1

# Different option but using internal assignment:
def rotate_smart(lst, amount):
    amount = amount % len(lst)
    backup = []
    for i in range(0, amount):
        backup.append(lst[i])

    for i in range(len(lst)):
        target = (i + amount) % len(lst)
        displaced = backup[i % amount]
        backup[i % amount] = lst[target]
        lst[target] = displaced

def check_rotate(rotate): # function that runs tests
    lst = [1, 2, 3, 4]
    rotate(lst, 1)
    assert lst == [4, 1, 2, 3]
    rotate(lst, -1)
    assert lst == [1, 2, 3, 4]
    rotate(lst, -2)
    assert lst == [3, 4, 1, 2]
    rotate(lst, -2)
    assert lst == [1, 2, 3, 4]
    lst.append(5)
    rotate(lst, 3)
    assert lst == [3, 4, 5, 1, 2]


def main():  # run tests
    check_rotate(rotate_naive)
    check_rotate(rotate_smart)


if __name__ == '__main__':
    main()
