from ib111 import week_04  # noqa

# ‹get_header› returns header of ‹table›.
def get_header(table: tuple[list[str], list[list[str | None]]]) -> list[str]:
    header, data = table
    return header


# ‹get_records› returns records of ‹table›.
def get_records(table: tuple[list[str], list[list[str | None]]]) -> list[list[str | None]] | list[None]:
    header, data = table
    return data

# Procedure ‹add_record› appends ‹record› to ‹table›.
def add_record(record: list[str | None], table: tuple[list[str], list[list[str | None]]]) -> tuple[list[str], list[list[str | None]]]:
    head, data = table
    if len(head) == len(record):
        data.append(record)
    return table

# Predicate ‹is_complete› is True, if ‹table› has zero ‹None› value.
def is_complete(table: tuple[list[str], list[list[str | None]]]) -> bool:
    header, data = table
    for row in data:
        for string in row:
            if string == None:
                return False
    return True

# ‹index_of_column› returns index of ‹name› column. Starts from 0.
def index_of_column(name: str, header: list[str]) -> int:
    index = 0
    for string in header:
        if string == name:
            return index
        index += 1
    return index

# ‹values› returns list of valid values in ‹name› column.
def values(name: str, table: tuple[list[str], list[list[str | None]]]) -> list[str | None]:
    header, rows = table
    index = index_of_column(name, header)
    values = []
    for row in rows:
        for i in range(len(row)):
            if index == i and row[i] != None:
                values.append(row[i])
    return values

# Procedure ‹drop_column› ‹name› column from table ‹table›. 
def drop_column(name: str, table: tuple[list[str], list[list[str | None]]]) -> tuple[list[str], list[list[str | None]]]:
    header, rows = table
    index = index_of_column(name, header)
    for i in range(len(header) - 1):
        if i >= index:
            header[i] = header[i + 1]
    header.pop()
    
    for row in rows:
        for y in range(len(row) - 1):
            if y >= index:
                row[y] = row[y + 1]
        row.pop()

    return table

def make_empty() -> tuple[list[str], list[list[str | None]]]:
    return ["A", "B", "C", "D"], []


def make_table() -> tuple[list[str], list[list[str | None]]]:
    return (["A", "B", "C"],
            [["a1", "b1", None],
             ["a2", "b2", "c2"],
             ["a3", None, "c3"]])


def main() -> None:

    # header test
    assert get_header(make_empty()) == ['A', 'B', 'C', 'D']
    assert get_header(make_table()) == ['A', 'B', 'C']

    # records test
    assert get_records(make_empty()) == []
    assert get_records(make_table()) == [["a1", "b1", None],
                                         ["a2", "b2", "c2"],
                                         ["a3", None, "c3"]]

    # add_record test
    tab_1 = make_empty()
    add_record(["a", "b", "c", "d"], tab_1)
    assert tab_1 == (['A', 'B', 'C', 'D'], [['a', 'b', 'c', 'd']])

    tab_2 = make_table()
    add_record(["a4", None, None], tab_2)
    assert tab_2 == (['A', 'B', 'C'],
                     [['a1', 'b1', None], ['a2', 'b2', 'c2'],
                      ['a3', None, 'c3'], ['a4', None, None]])

    # is_complete test
    assert is_complete(make_empty())
    assert not is_complete(make_table())
    assert is_complete((["A", "B", "C"],
                        [["a1", "b1", "c1"], ["a2", "b2", "c2"]]))

    # index_of_column test
    header = ['A', 'C', 'B']
    assert index_of_column('A', header) == 0
    assert index_of_column('C', header) == 1
    assert index_of_column('B', header) == 2

    tab_v = make_table()
    assert values("A", tab_v) == ["a1", "a2", "a3"]
    assert values("B", tab_v) == ["b1", "b2"]
    assert values("C", tab_v) == ["c2", "c3"]
    assert values("B", make_empty()) == []

    # drop_column test
    tab_3 = make_table()
    drop_column("A", tab_3)
    assert tab_3 == (['B', 'C'],
                     [['b1', None], ['b2', 'c2'], [None, 'c3']])

    tab_4 = make_table()
    drop_column("B", tab_4)
    assert tab_4 == (['A', 'C'],
                     [['a1', None], ['a2', 'c2'], ['a3', 'c3']])

    tab_5 = make_empty()
    drop_column("D", tab_5)
    assert tab_5 == (['A', 'B', 'C'], [])


if __name__ == "__main__":
    main()
