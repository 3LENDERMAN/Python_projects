from ib111 import week_06  # noqa

# Consider simple arithmetic expressions with addition and multiplication.
# We will store them in a pair of dictionaries (‹expr› and ‹const›), as follows
#:
#
# • the key is always the name of the variable (string),
# • the value in the dictionary ‹expr› is a triple:
# ◦ the first component is the operator ‹'*'› or ‹'+'›,
# ◦ the second and third components are the operands – the names of the variables,
# • the value in the dictionary ‹const› is a number.
#
# Each variable appears in at most one dictionary. Variables
# that are not in any of them are equal to zero.

# The function receives as parameters the dictionaries
# ‹expr› and ‹const› and the name of the variable. The result will be the value of this
# variable. When evaluating, you will need a stack and an auxiliary
# dictionary.

def evaluate(expr: dict[str, tuple[str, str, str]], const: dict[str, int], var: str) -> int:
    if len(expr) == 0: return const[var]
    all_vars: dict[str,int] = const.copy()
    while True:
        temp = all_vars.copy()
        for key, (op, a, b) in expr.items():
            if var in all_vars: return all_vars[var]
            if a in all_vars and b in all_vars:
                if op == "*": all_vars[key] = all_vars[a] * all_vars[b]
                else: all_vars[key] = all_vars[a] + all_vars[b]
        if all_vars == temp: break

    return all_vars[var]

def main() -> None: # tests
    assert evaluate({}, {'a': 1}, 'a') == 1
    assert evaluate({'x': ('+', 'a', 'a')}, {'a': 1}, 'x') == 2
    assert evaluate({'x': ('+', 'a', 'b')},
                    {'a': 1, 'b': 2}, 'x') == 3
    assert evaluate({'x': ('+', 'a', 'b'), 'y': ('*', 'x', 'x')},
                    {'a': 1, 'b': 2}, 'x') == 3
    assert evaluate({'x': ('+', 'a', 'b'), 'y': ('*', 'x', 'x')},
                    {'a': 1, 'b': 2}, 'y') == 9


if __name__ == "__main__":
    main()
