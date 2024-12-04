from ib111 import week_04  # noqa


# Function gets two positive integers ‹rows› and ‹cols› and returns table
# with ‹rows› rows and ‹cols› columns. On row ‹y› and column ‹x› 
# is number of common divisors ‹x› and ‹y›.

# Example ‹rows = 4›, ‹cols = 2› gets us ‹[[1,1], [1,2], [1,1], [1,2]]›.

def common_divisors(rows: int, cols: int) -> list[list[int]]:
    final = []
    for r_val in range(1, rows + 1):
        row = []
        for c_val in range(1, cols + 1):
            count = 0
            for x in range(1, max(rows, cols) + 1):
                if r_val % x == 0 and c_val % x == 0:
                    count += 1
            row.append(count)
        final.append(row)
    return final


def main() -> None:
    assert common_divisors(4, 2) == [[1, 1], [1, 2], [1, 1], [1, 2]]
    assert common_divisors(1, 1) == [[1]]
    assert common_divisors(1, 8) == [[1, 1, 1, 1, 1, 1, 1, 1]]
    assert common_divisors(5, 1) == [[1], [1], [1], [1], [1]]
    assert common_divisors(6, 6) == [[1, 1, 1, 1, 1, 1],
                                     [1, 2, 1, 2, 1, 2],
                                     [1, 1, 2, 1, 1, 2],
                                     [1, 2, 1, 3, 1, 2],
                                     [1, 1, 1, 1, 2, 1],
                                     [1, 2, 2, 2, 1, 4]]
    assert common_divisors(2, 4) == [[1, 1, 1, 1],
                                     [1, 2, 1, 2]]


if __name__ == '__main__':
    main()
