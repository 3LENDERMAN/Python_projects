from ib111 import week_01  # noqa

# Function returns how many coins do we need to pay (smallest number of coins)
# Coins are with value 1, 2 and 5 crowns.

def coins(value):
    count = 0
    while value > 0:
        if value >= 5: value -= 5
        elif value > 1: value -= 2
        else: value -= 1
        count += 1
    
    return count 


def main():
    assert coins(10) == 2
    assert coins(23) == 6
    assert coins(48) == 11
    assert coins(92) == 19
    assert coins(314) == 64
    assert coins(1043) == 210


if __name__ == "__main__":
    main()
