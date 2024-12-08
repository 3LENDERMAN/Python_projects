from ib111 import week_06  # noqa

# The robot can move forward and backward and rotate
# 90° in both directions. The robot's position is represented by a pair of integers;
# the first coordinate is ⟦x⟧ (negative numbers are west of
# the origin, positive ones are east), the second coordinate is ⟦y⟧ (negative
# numbers are north, positive ones are south).
#
# The pure function ⟦simulate_robot› receives a list of instructions for the robot,
# executes them, and returns the final position of the robot. At the beginning, the robot is at
# coordinates (0, 0) and is facing north. The individual
# instructions are pairs in this format:
#
# • ⟦("rotate", n)› – the robot rotates ⟦n⋅90°⟧ to the right (for negative
# ⟦n⟧ to the left);
# • ‹("forward", n)› – the robot moves forward ⟦n⟧ steps;
# • ‹("backward", n)› – the robot moves backward ⟦n⟧ steps;
# • ‹("undo", n)› – the robot undoes the effect of the last ⟦n⟧ executed
# instructions.
#
# For instructions other than ‹rotate›, ‹n› is always a non-negative integer.
# The ‹undo› instruction can be used multiple times, making it possible to undo
# the effect of multiple instructions, e.g. the sequence of instructions ‹forward 3›,
# ‹backward 7›, ‹undo 1›, ‹undo 1› will cause the robot to stand at
# its starting position.

def simulate_robot(instructions: list[tuple[str, int]]) -> tuple[int, int]:
    # Directions represented as NORTH,EAST,SOUTH,WEST
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_direction_index = 0  # start from north
    current_location = (0, 0)
    # Stack for history of states
    history = [(current_location, current_direction_index)]
    for instruction in instructions:
        command, steps = instruction
        if command == "forward":
            x,y = current_location
            dx, dy = directions[current_direction_index]
            current_location = (x + dx * steps, y + dy * steps)
        elif command == "backward":
            x, y = current_location
            dx, dy = directions[current_direction_index]
            current_location = (x - dx * steps, y - dy * steps)
        elif command == "rotate":
            # shift the direction 90 degrees left
            current_direction_index = (current_direction_index + steps) % 4
        elif command == "undo":
            # repetitevly delete last state from stack
            for _ in range(steps):
                history.pop()
            # set state to the last remaining state in the stack
            current_location, current_direction_index = history[-1]
            continue  # dont do undo
        # add state to history
        history.append((current_location, current_direction_index))
    a,b = current_location
    current_location = (b,a)
    return current_location

def main() -> None: # run tests
    assert simulate_robot([("forward", 100),
                           ("rotate", -1),
                           ("backward", 17),
                           ("rotate", 1),
                           ("rotate", 1),
                           ("rotate", 1),
                           ("undo", 1),
                           ("forward", 42)]) == (59, -100)
    assert simulate_robot([("forward", 1),
                           ("forward", 2),
                           ("forward", 5),
                           ("forward", 6),
                           ("undo", 1),
                           ("undo", 1),
                           ("forward", 3),
                           ("forward", 4)]) == (0, -10)

    cmds = [("rotate", -1), ("rotate", -1), ("rotate", -1)]
    assert simulate_robot(cmds) == (0, 0)
    assert cmds == [("rotate", -1), ("rotate", -1), ("rotate", -1)]

    cmds = [("backward", 1),
            ("backward", 2),
            ("rotate", -1),
            ("undo", 1),
            ("backward", 3),
            ("backward", 4)]
    assert simulate_robot(cmds) == (0, 10)
    assert cmds == [("backward", 1),
                    ("backward", 2),
                    ("rotate", -1),
                    ("undo", 1),
                    ("backward", 3),
                    ("backward", 4)]

    assert simulate_robot([("forward", 10000), ("backward", 10000)]) == (0, 0)
    assert simulate_robot([("rotate", -1), ("backward", 7)]) == (7, 0)
    assert simulate_robot([("forward", 100),
                           ("rotate", -1),
                           ("backward", 42),
                           ("undo", 1),
                           ("undo", 1),
                           ("forward", 2022),
                           ("undo", 1),
                           ("undo", 1),
                           ("rotate", 1),
                           ("backward", 7),]) == (-7, 0)


if __name__ == '__main__':
    main()
