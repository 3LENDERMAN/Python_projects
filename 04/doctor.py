from ib111 import week_04  # noqa


# function working with a list of patients ‹patients› at a doctor.
# patient has a record (double) that contains his unique identifier and a list
# of visits with results. A visit is represented by a quartet – the year,
# when the patient visited the doctor, and the measured values: pulse,
# systolic and diastolic pressure.

# ‹missing_visits›, returns patients who have not been seen since ‹year›.
# Return a list of patient identifiers as a result.
# patient = (id, visits[(year, pulse, sys, dia),(2016, 80, 135, 65),(...)])
Patient = tuple[int, list[tuple[int, int, int, int]]]

def missing_visits(year: int, patients: list[Patient]) -> list[int]:
    missing = []
    for patient in patients:
        ico, visits = patient
        visit = visits[len(visits) - 1]
        date, _, _, _ = visit
        if date <= year:
            missing.append(ico)
    return missing

# ‹patient_reports› returns a list of patient reports.
# A patient report is a quartet, containing a record of the patient's highest heart rate ever measured and, for
# each measured value, whether the measurements of that value
# have been consistently increasing over the years (‹True› or ‹False›).

# For example, a patient report ‹(1, [(2015, 91, 120, 80), (2018,
# 89, 125, 82), (2020, 93, 120, 88)])› is ‹(93, False, False,
# True)›.

def patient_reports(patients: list[Patient]) -> list[tuple[int, bool, bool, bool]]:
    reports = []
    for patient in patients:
        sys = 0
        sys_p = True
        dia = 0
        dia_p = True
        pulse = 0
        pul_p = True
        ico, visits = patient
        for visit in visits:
            _, p, s, d = visit
            if s > sys: sys = s
            else: sys_p = False
            if d > dia: dia = d
            else: dia_p = False
            if p > pulse: pulse = p
            else: pul_p = False
        report = (pulse, pul_p, sys_p, dia_p)
        reports.append(report)
    return reports


def main() -> None:
    p1 = (0, [(2016, 102, 140, 95)])
    p2 = (1, [(2015, 91, 120, 80), (2018, 89, 125, 82),
              (2020, 93, 120, 88)])
    p3 = (2, [(2010, 73, 110, 70), (2015, 75, 112, 70),
              (2017, 76, 114, 71), (2019, 79, 116, 72)])
    p4 = (3, [(2016, 82, 115, 82), (2017, 83, 117, 80)])
    p5 = (4, [(2005, 81, 130, 90), (2007, 81, 130, 90),
              (2011, 80, 130, 90), (2013, 81, 130, 90),
              (2017, 82, 130, 90)])

    p6 = (5, [(2000, 74, 120, 80), (2011, 107, 142, 95),
              (2012, 94, 140, 97)])
    p7 = (6, [(2019, 101, 145, 95), (2020, 101, 145, 95)])

    patients = [p1, p2, p3, p4, p5]
    assert missing_visits(2017, patients) == [0, 3, 4]
    assert missing_visits(2016, patients) == [0]
    assert missing_visits(2000, patients) == []

    assert patient_reports(patients) == \
        [(102, True, True, True), (93, False, False, True),
         (79, True, True, False), (83, True, True, False),
         (82, False, False, False)]

    assert patient_reports([p6, p7]) == \
        [(107, False, False, True), (101, False, False, False)]


if __name__ == "__main__":
    main()
