from ib111 import week_05  # noqa

# Two lists consists of integers, ‹largest_common_sublist_sum›,
# finds that sublist of ‹left› and ‹right› which has biggest sum.

# Sublist of list ‹S› means ‹T› for which exists ‹k› where applies ‹S[k + i] == T[i]› 
# for all ‹i› that ⟦0 ≤ i < len(T)⟧
# Example: ‹[1, 2]› is sublist of list ‹[0, 1, 2, 3]› where ‹k = 1›.

def largest_common_sublist_sum(left: list[int], right: list[int]) -> int:
    max_sum = 0
    for length in range(1, len(left) + 1):
        for start_left in range(len(left) - length + 1):
            current_sum = 0
            match = True
            for i in range(length):
                current_sum += left[start_left + i]
            for start_right in range(len(right) - length + 1):
                match = True
                for i in range(length):
                    if left[start_left + i] != right[start_right + i]:
                        match = False
                        break
                if match:
                    max_sum = max(max_sum, current_sum)
    return max_sum

def main() -> None: # run tests
    l1: list[int] = []
    l2 = [1, 2, 3, 4, 5]
    l3 = [2, 3, 4, 6, 7, 9, 10]
    l4 = [1, 2, 3, 8, 9]

    assert largest_common_sublist_sum(l1, l2) == 0
    assert largest_common_sublist_sum(l2, l3) == 9
    assert largest_common_sublist_sum(l2, l4) == 6
    assert largest_common_sublist_sum(l3, l4) == 9


if __name__ == "__main__":
    main()
