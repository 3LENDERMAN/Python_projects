from ib111 import week_06  # noqa


# Clear function gets:
# • a non-empty expression ‹expr› composed of variables and arithmetic
# operators, written in postfix notation, and
# • a dictionary, assigning a numeric value to variables
#
# and returning the number to which the given expression is evaluated. Each operator
# or variable is a separate string, the entire expression is then formed
# by a sequence of these strings. The only allowed operators are ‹+› and
# ‹*›.

# Postfix notation works as follows:
# • we read the expression from left to right, writing down each value,
# • when we encounter an operator, e.g. ‹+›:
# ◦ in the head we add up the last two values ​​we wrote,
# ◦ we delete these values,
# ◦ we write down the sum we remembered instead.
#
# We repeat this procedure until we have read the entire expression. If the
# expression is correctly formed, at the end of this process we have a single number written
# This number is the result of evaluating the entered expression.

def rpn_eval(expr: list[str], variables: dict[str, int]) -> int:
    if len(expr) == 1: return variables[expr[0]]
    stack: list[int] = []
    for value in expr:
        if value == "+":
            stack[len(stack) - 2] += stack[len(stack) - 1] 
            stack.pop()
        elif value == "*":
            stack[len(stack) - 2] *= stack[len(stack) - 1] 
            stack.pop()
        else: stack.append(variables[value])
    return stack[0]

def main() -> None: # tests
    assert rpn_eval(["a"], {"a": 5}) == 5
    assert rpn_eval(["a", "b", "+"], {"a": 1, "b": -4}) == -3
    assert rpn_eval(["x", "y", "+"], {"x": 1, "y": 2}) == 3
    assert rpn_eval(["x", "y", "+", "y", "*", "z", "+"],
                    {"x": 5, "y": 2, "z": 25}) == 39
    assert rpn_eval(["x", "x", "*", "x", "*"],
                    {"x": 5}) == 125
    assert rpn_eval(["a", "a", "a", "a", "a", "a", "+", "+", "+",
                     "+", "+"], {"a": 1}) == 6

if __name__ == '__main__':
    main()
