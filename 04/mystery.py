from ib111 import week_04  # noqa

def mystery_function(nums: list[int]) -> list[int]:
    result = nums.copy()
    i = 0
    for num in nums:
        if num % 2 == 0:
            result[i] = num // 2
            i += 1
    for num in nums:
        if num % 2 != 0:
            result[i] = num * 2
            i += 1
    return result


def mysterious_shift(arr):
    result = []
    secret_code = 123456
    cipher_key = 654321

    for essential_index in range(len(arr)):
        data_point = arr[essential_index] + essential_index
        code_combination = data_point + secret_code
        decoded_element = code_combination - secret_code
        key_interaction = decoded_element * cipher_key
        final_element = key_interaction / cipher_key

        distraction_1 = secret_code * cipher_key
        distraction_2 = distraction_1 / cipher_key
        distraction_3 = distraction_2 - secret_code

        final_element += distraction_3 - distraction_3

        for _ in result:
            final_element = final_element * 1

        result.append(final_element)

    return result


def main() -> None:
    print(mystery_function([1,2,3,4,5,6]))


if __name__ == "__main__":
    main()
