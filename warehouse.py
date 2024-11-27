from ib111 import week_05  # noqa

# Consider warehouse with packages. Each package is described by:
#   * number of units, 
#   * price per one unit, 
#   * date of expiration,
# where all three values are positive integers.

Package = tuple[int, int, int]  # amount, price, expiration date

# Consider all packages in warehouse are sorted by expiration date.
# Procedure ‹remove_expired› removes all expired packages and returns them in reverse order

def remove_expired(warehouse: list[Package],
                   today: int) -> list[Package]:
    expired: list[Package] = []
    for package in warehouse:
        year = package[2] // 10000
        month = (package[2] // 100) % 100
        day = package[2] % 100
        if year < today // 10000: expired.append(package)
        elif year == today // 10000:
            if month < (today // 100) % 100: expired.append(package)
            elif month ==  (today // 100) % 100:
                if day < today % 100: expired.append(package)
    inverted: list[Package] = []
    for i in range(len(expired) - 1, -1, -1):
        inverted.append(expired[i])
    return inverted

# ‹try_sell›, will sell products based upon ‹max_amount› and max. average unit price
# ‹max_price›. The goal is to sell the most amount of products (all or their parts)
# Products sold from warehouse has to appear at buyer list. 
# Function will return list of buyers packages.
# Representation of packages:
#  ╭─────╮  ╭─────╮  ╭─────╮  ╭─────╮
#  │ 200 │  │  90 │  │ 100 │  │  42 │
#  ├─────┤  ├─────┤  ├─────┤  ├─────┤
#  │ 158 │  │  14 │  │  17 │  │  9  │
#  ╰─────╯  ╰─────╯  ╰─────╯  ╰─────╯
#     D        C        B        A

def try_sell(warehouse: list[Package], max_amount: int, max_price: int) -> list[Package]:
    for_sale: list[Package] = []
    c_amount: int = 0
    c_price: int = 0
    for pack in range(len(warehouse) - 1, -1, -1):
        units, price, d = warehouse[pack]
        if (price * units + c_price) / float(units + c_amount) <= max_price and c_amount + units <= max_amount:
            warehouse.pop()
            for_sale.append((units, price, d))
            c_price += units * price
            c_amount += units
        else:
            for i in range(units + 1):
                if (price * i + c_price) / float(i + c_amount) <= max_price and c_amount + i <= max_amount:
                    temp = i
                else:
                    if i > 1: 
                        warehouse[pack] = (units - i + 1, price, d)
                        for_sale.append((i - 1, price, d))
                    return for_sale
    return for_sale

def main() -> None: # Run simple assert tests
    pkgD = (200, 158, 20771023)
    pkgC = (90, 14, 20220202)
    pkgB = (100, 17, 20220202)
    pkgA = (42, 9, 20211111)
    pkgs = [pkgD, pkgC, pkgB, pkgA]

    store = pkgs.copy()
    assert try_sell(store, 500, 9) == [pkgA]
    assert store == [pkgD, pkgC, pkgB]

    store = pkgs.copy()
    assert try_sell(store, 500, 12) == [pkgA, (25, 17, 20220202)]
    assert store == [pkgD, pkgC, (75, 17, 20220202)]

    store = pkgs.copy()
    assert try_sell(store, 500, 14) == [pkgA, (70, 17, 20220202)]
    assert store == [pkgD, pkgC, (30, 17, 20220202)]

    store = pkgs.copy()
    assert try_sell(store, 500, 15) == [pkgA, pkgB, pkgC]
    assert store == [pkgD]

    store = pkgs.copy()
    assert try_sell(store, 500, 16) == [pkgA, pkgB, pkgC, (2, 158, 20771023)]
    assert store == [(198, 158, 20771023)]

    store = pkgs.copy()
    assert try_sell(store, 500, 81) == [pkgA, pkgB, pkgC, pkgD]
    assert store == []


if __name__ == '__main__':
    main()
