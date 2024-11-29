from ib111 import week_03
from math import sqrt

# Calculation of simple statistics over elements of a given list:
# mean, median, and standard deviation.
def average(data): # get average value
    return float(sum(data)) / len(data)

# consider input to be sorted:
def median(data):
    # Find median value from indexes:
    if len(data) % 2 == 1:
        # for odd, take value in the middle
        return data[len(data) // 2]

    else:
        # for even, take average of two middle values
        return float(data[len(data) // 2] +
                     data[len(data) // 2 - 1]) / 2

# «standard deviation» ⟦s⟧. Calculated as the square root of the «variance» ⟦s²⟧
# described by the following relationship: ⟦ s² = 1/(n - 1) ∑ᵢ₌₁ⁿ (xᵢ - m)² ⟧

def stddev(data):
    mean = average(data)
    square_error_sum = 0.0

    for x_i in data:
        square_error_sum += (x_i - mean) ** 2

    variance = square_error_sum / (len(data) - 1)

    return sqrt(variance)

def main(): # run simple tests
    assert median([1, 2, 3]) == 2
    assert median([1, 3]) == 2

    sample = [2, 4, 4, 4, 5, 5, 5, 7, 9]
    assert average(sample) == 5
    assert median(sample) == 5
    assert stddev(sample) == 2


if __name__ == '__main__':
    main()
