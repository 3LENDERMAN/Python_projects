from ib111 import week_06  # noqa

# A function that receives a signal ‹data›
# represented by a list of integer amplitudes (samples).
# The result will be statistics for this signal, which it creates
# in the following way:

# 1. the function first cleans the signal of all samples with an amplitude
# greater than ‹max_amplitude› and less than ‹min_amplitude›,
# 2. then resamples it by merging each ‹bucket›
# sample (the last sample may be incomplete) into one
# by calculating their average and then rounding it
# (using the built-in ‹round› function),
# 3. finally counts how many times each amplitude appears
# in the adjusted signal, and returns a dictionary where the key will be the amplitude
# and the value will be the number of its occurrences.

def histogram(data: list[int], max_amplitude: int, min_amplitude: int, bucket: int) -> dict[int, int]:
    filtered_data = []
    for value in data:
        if min_amplitude <= value <= max_amplitude:
            filtered_data.append(value)
        resampled_data = []
    count = 0
    sum_bucket = 0
    for value in filtered_data:
        sum_bucket += value
        count += 1
        if count == bucket:
            average = round(sum_bucket / float(bucket))
            resampled_data.append(average)
            count = 0
            sum_bucket = 0
    if count > 0:
        average = round(sum_bucket / float(count))
        resampled_data.append(average)

    histogram: dict[int,int] = dict()
    for value in resampled_data:
        if value in histogram:
            histogram[value] += 1
        else:
            histogram[value] = 1

    return histogram

def main() -> None: # tests
    data = [1, 1, 1]
    assert histogram(data, 5, 0, 1) == {1: 3}
    assert data == [1, 1, 1]

    assert histogram([1, 1, 1, 1], 5, 0, 2) == {1: 2}
    assert histogram([1, 2, 3, 4, 5], 5, 2, 2) == {2: 1, 4: 1}
    assert histogram([1, 2, 9, 2, 10, 1, 1, 1, 1], 8, 1, 3) == {2: 1, 1: 2}

    data = []
    assert histogram([], 1, 2, 5) == {}
    assert data == []

    assert histogram([1, 1, 1, 8, 8, 8], 5, 3, 10) == {}
    assert histogram([1, 2, 3, 4], 2, 5, 3) == {}
    assert histogram([1, 2, 3, 4, 5], 10, 1, 7) == {3: 1}


if __name__ == '__main__':
    main()
