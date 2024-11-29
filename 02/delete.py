from ib111 import week_02  # noqa

# Function ‹delete_to_maximal› for ‹number› returns biggest
# value by deleting one decimal digit in number.

def delete_to_maximal(number):
    original_number = number
    current_power_of_ten = 1
    max_number = float('-inf')  # Initialize to smallest number

    while current_power_of_ten <= original_number:
        left_part = number // (current_power_of_ten * 10) 
        right_part = number % current_power_of_ten  
        new_number = left_part * current_power_of_ten + right_part
        max_number = max(max_number, new_number)
        current_power_of_ten *= 10

    return max_number

def get_length(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count

# Function ‹delete_k_to_maximal› returns biggest number created by deleting <k> digits:

def delete_k_to_maximal(number, k):
    result = number
    for i in range(k):
        result = delete_to_maximal(result)

    return result

def main():
    assert delete_to_maximal(54) == 5
    assert delete_to_maximal(45) == 5
    assert delete_to_maximal(100) == 10
    assert delete_to_maximal(123) == 23
    assert delete_to_maximal(4312) == 432
    assert delete_to_maximal(1231) == 231
    assert delete_to_maximal(2331) == 331

    assert delete_k_to_maximal(2331, 2) == 33
    assert delete_k_to_maximal(22331, 2) == 331
    assert delete_k_to_maximal(12345, 4) == 5
    assert delete_k_to_maximal(1234554321, 8) == 55
    assert delete_k_to_maximal(123123123123, 4) == 33123123
    assert delete_k_to_maximal(123321123321, 4) == 33223321
    assert delete_k_to_maximal(11181118111, 9) == 88


if __name__ == "__main__":
    main()
