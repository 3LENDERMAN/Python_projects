from ib111 import week_03  # noqa

# Similiar to ‹cellular› but procedure (direct modification of input list) 

# Rules:
# │‹old[i]›│‹old[i + 1]›│‹old[i + 2]›│‹new[i]›│
# ├┄┄┄┄┄┄┄┄┼┄┄┄┄┄┄┄┄┄┄┄┄┼┄┄┄┄┄┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄│
# │    1   │      0     │      0     │    0   │
# │    0   │      1     │      0     │    1   │
# │    0   │      1     │      1     │    1   │
# │    1   │      0     │      1     │    0   │
# │    1   │      1     │      1     │    0   │

def cellular_in_situ(state):
    for i in range(len(state)):
        if i == len(state) - 2:
            state[i] = rules(state[i] * 100 + state[i + 1] * 10)
        elif i == len(state) - 1:
            state[i] = rules(state[i] * 100)
        else:
            state[i] = rules(state[i] * 100 + state[i + 1] * 10 + state[i + 2])

def rules(n):
    if n == 100 or n == 101 or n == 111:
        return 0
    elif n == 10 or n == 11:
        return 1
    n //= 10
    return n % 10

def main(): # run tests
    state = [1, 0, 0, 1, 1, 0]
    cellular_in_situ(state)
    assert state == [0, 0, 1, 1, 0, 0]
    cellular_in_situ(state)
    assert state == [0, 1, 1, 0, 0, 0]

    state = []
    cellular_in_situ(state)
    assert state == []

    state = [1, 1, 1, 1]
    cellular_in_situ(state)
    assert state == [0, 0, 1, 0]
    cellular_in_situ(state)
    assert state == [0, 1, 0, 0]


if __name__ == "__main__":
    main()
