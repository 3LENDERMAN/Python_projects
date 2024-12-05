from ib111 import week_05  # noqa


# System of attendance in company. Each employee has to swipe with card
# at the entrance and same when leaving.

# Sensor at the door evidates the records. Each record consists of employee id, 
# time stamp and type of record (leaving, entrance) 

EmployeeId = str  # employee id
TimeStamp = int  # number of seconds from specific time
RecordType = bool  # type of record

ENTRY = True
LEAVE = False

MachineRecord = tuple[EmployeeId, TimeStamp, RecordType]

# ‹employees_with_missing_records› returns set of employees who has some discrepancy
# either came to work and never left or came many times without leaving.
# Consider input list to be sorted by time stamps.

def employees_with_missing_records(records: list[MachineRecord]) -> set[EmployeeId]:
    temp_lst: list[tuple[str, bool | None]] = []
    missing: set[str] = set()
    if len(records) == 0: return missing
    temp_dic: dict[str, bool | None] = dict(temp_lst)
    for ids, data, rec in records:
        if ids not in temp_dic and rec != None:
            if rec: temp_dic[ids] = rec
            else: 
                temp_dic[ids] = None
                missing.add(ids)
        else:
            if temp_dic[ids] != rec: temp_dic[ids] = rec
            else: 
                temp_dic[ids] = None
                missing.add(ids)
    return missing

def main() -> None: # tests
    id1 = "abc00001"
    id2 = "xyz00002"
    id3 = "hjkl0003"

    e1 = (id1, 100, ENTRY)
    e2 = (id2, 110, ENTRY)
    e3 = (id3, 140, ENTRY)
    e4 = (id1, 200, ENTRY)
    e5 = (id1, 300, ENTRY)

    l1 = (id1, 150, LEAVE)
    l2 = (id2, 160, LEAVE)
    l3 = (id3, 210, LEAVE)
    l4 = (id1, 250, LEAVE)
    l5 = (id2, 270, LEAVE)

    # no missing records
    m1 = employees_with_missing_records([])
    assert len(m1) == 0

    m2 = employees_with_missing_records([e1, l1])
    assert len(m2) == 0

    m3 = employees_with_missing_records([e1, e2, l1, l2, e4])
    assert len(m3) == 0

    m4 = employees_with_missing_records([e1, e3, l1, e4, l3, l4])
    assert len(m4) == 0

    # missing records
    m5 = employees_with_missing_records([e1, l1, e4, e5])
    assert len(m5) == 1
    assert id1 in m5

    m6 = employees_with_missing_records([e1, e2, l1, l2, l5])
    assert len(m6) == 1
    assert id2 in m6

    m7 = employees_with_missing_records([e1, e4, l5])
    assert len(m7) == 2
    assert id1 in m7
    assert id2 in m7


if __name__ == "__main__":
    main()
