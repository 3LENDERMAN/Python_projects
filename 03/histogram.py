from ib111 import week_03  # noqa

# histogram for list ‹data› returns list of tuples – number and its appearance. 
# Output list has to be sorted by first member in tuple
# Consider input interval to be [0, 100] (including).

def histogram(data):
    numbers = []
    if data == []:
        return []
    for i in range(101):
        count = 0
        for num in data:
            if num == i:
                count += 1
        if count > 0:
            numbers.append((i, count))

    return numbers

def main() -> None: # run tests
    assert histogram([1, 2, 3, 2, 1]) == [(1, 2), (2, 2), (3, 1)]
    assert histogram([7, 1, 7, 1, 5]) == [(1, 2), (5, 1), (7, 2)]
    assert histogram([1, 1, 1]) == [(1, 3)]
    assert histogram([]) == []


if __name__ == "__main__":
    main()
