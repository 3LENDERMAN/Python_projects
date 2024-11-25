from ib111 import week_01  # noqa


# Consider a four-player game with the following rules:
# • the game board is one-dimensional, with unlimited length and a marked starting point by box;
# • each player has one piece, initially placed on the starting square;
# • players take turns rolling the dice and moving their pieces by the rolled number;
# • if a player's piece should enter a square occupied by a piece, figure is "kicked"
#
# Situation on the game board using a non-negative integer
# so that its notation in the five system represents the occupancy of individual
# field without starting field. The digit 0 represents an empty box,
# numbers 1-4 then represent the occupancy of a particular player's piece. Movement
# of figures in fives notation runs "from right to left", i.e. from
# of lower orders to higher.
#
# Example:
#  ┌───────────┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
#  │start: 1234│   │   │   │   │   │   │   │   │   │   │   │ …
#  └───────────┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
#
# All players are placed at the start - number 0.
#  ┌───────────┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
#  │start: 1 3 │   │ 2 │   │   │   │ 4 │   │   │   │   │   │ …
#  └───────────┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
#
# Players 1 and 3's pieces are at the start, player 2's piece is two squares from the start,
# player 4's piece is six spaces from the start. This state is represented
# by the number ⟦(400020)₅ = 4 · 5⁵ + 2 · 5¹ = 12510⟧.
#
# Function ‹play› game board represented by the number ‹arena›
# makes one move of ‹player› by the specified ‹throw› dice and returns
# a number representing the new state of the game.

def play(arena, player, throw):
    if throw == 0: return arena
    if arena == 0: return player * (10 ** (throw - 1))
    game = to_different_base(arena, 5)
    player_index = 0
    temp = game
    i = 0
    while temp > 0:
        if temp % 10 == player:
            player_index = i + 1
        temp //= 10
        i += 1
    temp = game
    for j in range(player_index + throw):
        if temp == 0: future_play = 0; continue 
        else: future_play = temp % 10
        temp //= 10
    if player_index != 0:
        game -= player * (10 ** (player_index - 1))
    if future_play != 0:
        game -= future_play * (10 ** (player_index + throw - 1))
    game += player * (10 ** (player_index + throw - 1))
    return to_different_base(game, 10)

def to_different_base(num: int, base: int) -> int:
    if num == 0: return 0
    val = 0
    if base == 5: add = 10
    else: add = 5
    power = 1
    while num > 0:
        val += (num % base) * power
        num //= base
        power *= add
    return val

def main():
    for p in range(1, 5):
        assert play(0, p, 1) == p

    assert play(11, 3, 3) == 86
    assert play(84770, 4, 5) == 147250
    assert play(84770, 3, 4) == 240645
    assert play(12510, 1, 2) == 12505


if __name__ == '__main__':
    main()
