from ib111 import week_03  # noqa


# Procedure ‹partition› gets on input list of numbers ‹data› and valid index ‹idx› 
# ‹data[idx]› = ‹pivot›.

# Procedure sorts list so all numbers smaller than pivot move to left and bigger on right
# from the <pivot>

# It will create list:
#   • numbers smaller than ‹pivot›
#   • pivot
#   • numbers bigger than ‹pivot›

# For ‹[3, 4, 1, 2, 0]› and index ‹0›: ‹[1, 0, 2, 3, 4]› or ‹[1, 2, 0, 3, 4]›.

def partition(data, idx):
    shuffle = True
    while shuffle:
        shuffle = False
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                shuffle = True

def main(): # run tests
    run_test([3, 4, 6, 2, 5], 4)
    run_test([0, 1, 3, 4, 6, 2, 5], 4)
    run_test([0, 1, 3, 4, 6, 2, 5], 2)
    run_test([0, 2, 1, 5, 6, 9], 0)
    run_test([0, 2, 1, 5, 6, 9], 3)
    run_test([6, 9, 3, 0, 1], 2)


def run_test(data, idx):
    pivot = data[idx]
    count = len(data)
    sum_ = sum(data)

    partition(data, idx)

    assert len(data) == count
    assert sum(data) == sum_

    i = 0

    while i < count and data[i] < pivot:
        i += 1
    while i < count and data[i] == pivot:
        i += 1
    while i < count and data[i] > pivot:
        i += 1

    assert i == count


if __name__ == "__main__":
    main()
