from ib111 import week_05  # noqa

# Same system of attendance as in previous project

EmployeeId = str  # employee id
TimeStamp = int  # number of seconds from some point in time
RecordType = bool  # type of record

ENTRY = True
LEAVE = False

MachineRecord = tuple[EmployeeId, TimeStamp, RecordType]

# Based on working hours, company calculates employee revenue. 
# Clear function ‹seconds_spent_working› returns, how many seconds each employee worked.
# Considered list is sorted by time and there are no mistakes in records 

def seconds_spent_working(records: list[MachineRecord]) -> dict[EmployeeId, int]:
    lst: list[tuple[str, int]] = []
    time_dict: dict[str, int] = dict(lst)
    for ids, time, rec in records:
        if ids not in time_dict: time_dict[ids] = time
        else: time_dict[ids] = (time_dict[ids] - time) * -1
    return time_dict

def main() -> None: # run tests
    id1 = "abc00001"
    id2 = "xyz00002"
    id3 = "hjkl0003"

    e1 = (id1, 100, ENTRY)
    e2 = (id2, 110, ENTRY)
    e3 = (id3, 140, ENTRY)
    e4 = (id1, 200, ENTRY)

    l1 = (id1, 150, LEAVE)
    l2 = (id2, 160, LEAVE)
    l3 = (id3, 210, LEAVE)
    l4 = (id1, 250, LEAVE)

    t1 = seconds_spent_working([e1, l1])
    assert len(t1) == 1
    assert t1[id1] == 50

    t2 = seconds_spent_working([e2, e3, l2, l3])
    assert len(t2) == 2
    assert t2[id2] == 50
    assert t2[id3] == 70

    t3 = seconds_spent_working([e1, l1, e4, l4])
    assert len(t3) == 1
    assert t3[id1] == 100

    t4 = seconds_spent_working([e1, e2, e3, l1, l2, e4, l3, l4])
    assert len(t4) == 3
    assert t4[id1] == 100
    assert t4[id2] == 50
    assert t4[id3] == 70


if __name__ == "__main__":
    main()
