from ib111 import week_06  # noqa

# The pure function ‹valid_stack_ops› takes two lists
# ‹pushed›, ‹popped› as input and decides whether these lists could have been
# the result of a sequence of «push» and «pop» operations on a stack
# that is initially empty. (The list ‹pushed› should correspond to the order
# in which the elements were inserted by the «push» operation; the list ‹popped› to the order
# in which the elements were removed by the «pop» operation.)
#
# Examples:
# For the input ‹([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])› the result should be
# ‹True›, because there is a sequence of operations «push 1», «push 2»,
# «push 3», «push 4», «pop» (returns 4), «push 5», «pop» (returns 5),
# «pop» (returns 3), «pop» (returns 2), «pop» (returns 1).
#
# For the input ‹([1, 2, 3, 4, 5], [4, 3, 5, 1, 2])› the result should be
# ‹False› because there is no sequence of «push»
# and «pop» operations that would match these lists.

def valid_stack_ops(pushed: list[int], popped: list[int]) -> bool:
    stack: list[int] = []
    curr_index = 0  
    for item in pushed:
        stack.append(item)
        while stack and curr_index < len(popped) and stack[-1] == popped[curr_index]:
            stack.pop()
            curr_index += 1
    return curr_index == len(popped)

def main() -> None:
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    assert valid_stack_ops(pushed, popped)
    assert pushed == [1, 2, 3, 4, 5]
    assert popped == [4, 5, 3, 2, 1]

    assert not valid_stack_ops([1, 2, 3, 4, 5], [4, 3, 5, 1, 2])
    assert valid_stack_ops([1, 2, 3, 4, 5], [3, 5])
    assert valid_stack_ops([], [])
    assert not valid_stack_ops([], [1])

    pushed = [1, 2, 3, 4, 5]
    popped = [3, 5, 2]
    assert not valid_stack_ops(pushed, popped)
    assert pushed == [1, 2, 3, 4, 5]
    assert popped == [3, 5, 2]

    assert valid_stack_ops(
        [42, 17, 1729, 1337, 1, 2, 3, 10, 11, 12, 1000, 0, -17, 7],
        [17, 1337, 1729, 3, 2, 12, 11, -17, 0, 1000, 7],
    )


if __name__ == '__main__':
    main()
