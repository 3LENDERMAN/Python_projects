from ib111 import week_06  # noqa

# The robotic frog jumps straight ahead a specified distance and rotates 90° in both directions.
#
# The pure function ‹simulate_frogbot› receives a list of instructions for the robotic frog,
# executes them, and returns the number of different positions the frog was in during the execution of
# the instructions (including the starting and ending positions).
#
# The individual instructions are pairs in this format:
#
# • ‹("rotate", n)› – the robotic frog rotates ⟦n⋅90°⟧ (positive angle
# to the right, negative angle
# to the left);
# • ‹("jump", n)› – the robotic frog jumps ⟦n⟧ units forward.
#
# Here ⟦n⟧ can be any positive integer (the function must work without
# problems even for huge numbers).

def simulate_frogbot(instructions: list[tuple[str, int]]) -> int:
    direction: list[tuple[int,int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_direction_index = 0
    current_position: tuple[int, int] = (0, 0)
    set_of_positions: set[tuple[int,int]] = {(0,0)}
    for instruction in instructions:       
        comm, step = instruction
        if comm == "rotate":
            current_direction_index = (current_direction_index + step) % 4
        elif comm == "jump":
            x, y = current_position
            rot_x, rot_y = direction[current_direction_index]
            current_position = (x + (rot_x * step), y + (rot_y * step)) 
        set_of_positions.add(current_position)
    return len(set_of_positions)

def main() -> None: #tests
    assert simulate_frogbot([("jump", 100),
                             ("rotate", -1),
                             ("jump", 17),
                             ("rotate", 1),
                             ("rotate", 1),
                             ("jump", 42)]) == 4

    cmds = [("jump", 1), ("jump", 2), ("jump", 3), ("jump",  4)]
    assert simulate_frogbot(cmds) == 5
    assert cmds == [("jump", 1), ("jump", 2), ("jump", 3), ("jump",  4)]

    assert simulate_frogbot([("rotate", -1), ("rotate", -1),
                             ("rotate", -1)]) == 1

    cmds = [("jump", 2), ("rotate", -1), ("rotate", -1), ("jump", 2)]
    assert simulate_frogbot(cmds) == 2
    assert cmds == [("jump", 2), ("rotate", -1), ("rotate", -1), ("jump", 2)]

    assert simulate_frogbot([("jump", 7),
                             ("rotate", 1),
                             ("jump", 10000),
                             ("rotate", 1),
                             ("rotate", 1),
                             ("jump", 10000),
                             ("rotate", -1),
                             ("jump", 7),
                             ("rotate", 1)]) == 3
    assert simulate_frogbot([("jump", 5),
                             ("rotate", -1),
                             ("rotate", -1),
                             ("jump", 2),
                             ("jump", 3)]) == 3
    assert simulate_frogbot([("jump", 1),
                             ("jump", 4),
                             ("rotate", 1),
                             ("jump", 4),
                             ("rotate", 1),
                             ("jump", 2),
                             ("rotate", 1),
                             ("jump", 1),
                             ("rotate", -1),
                             ("jump", 2),
                             ("rotate", 1),
                             ("jump", 3),
                             ("jump", 17)]) == 8


if __name__ == '__main__':
    main()
