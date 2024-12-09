from ib111 import week_06  # noqa

# Nonempty tree with numeric nodes (root is always 1), example:
#
#             ┌───┐
#             │ 1 │
#             └───┘
#          ╭───╯ ╰─────╮
#          ▼           ▼
#        ┌───┐       ┌───┐
#        │ 2 │       │ 3 │
#        └───┘       └───┘
#    ╭────╯│╰────╮     │
#    │     │     │     │
#    ▼     ▼     ▼     ▼
#  ┌───┐ ┌───┐ ┌───┐ ┌───┐
#  │ 4 │ │ 5 │ │ 6 │ │ 7 │
#  └───┘ └───┘ └───┘ └───┘
#
# This tree is encoded into dictionary like:

Tree = dict[int, list[int]]


def example_tree() -> Tree:
    return {1: [2, 3],
            2: [4, 5, 6],
            3: [7],
            4: [], 5: [], 6: [], 7: []}

# So the keys are the vertex numbers and the values ​​are lists of their
# (direct) descendants. Write a pure function that finds the "longest
# row" in the image of such a tree and returns its length. A row is
# always made up of nodes that are the same distance from the root.

def breadth(tree: Tree) -> int:
    if not tree: return 0
    current_level = [1]
    max_width = 0

    while current_level:
        max_width = max(max_width, len(current_level))
        next_level = []
        for node in current_level:
            next_level.extend(tree[node])
        current_level = next_level

    return max_width

def main() -> None: # tests
    assert breadth({1: []}) == 1
    assert breadth({1: [2], 2: []}) == 1
    assert breadth({1: [2], 2: [3, 4], 3: [], 4: []}) == 2

    assert breadth(example_tree()) == 4

    big_tree: Tree = {1: [2, 3, 4], 2: [], 3: [5, 6], 4: [7],
                      5: [8, 9, 10], 6: [11], 7: [], 8: [],
                      9: [12], 10: [], 11: [], 12: []}
    assert breadth(big_tree) == 4


if __name__ == "__main__":
    main()
