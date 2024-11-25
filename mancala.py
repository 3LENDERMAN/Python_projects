from ib111 import week_03  # noqa

# The game board consists of two rows of smaller holes (their number is a parameter
# of games, see below) and two larger dimples left and right. So it looks like thus
# (the number of smaller dimples in each row here is six):
#
#  ╭───────╮╭───╮╭───╮╭───╮╭───╮╭───╮╭───╮╭───────╮
#  │       ││ M ││ L ││ K ││ J ││ I ││ H ││       │
#  │   N   │╰───╯╰───╯╰───╯╰───╯╰───╯╰───╯│       │
#  │       │╭───╮╭───╮╭───╮╭───╮╭───╮╭───╮│   G   │
#  │       ││ A ││ B ││ C ││ D ││ E ││ F ││       │
#  ╰───────╯╰───╯╰───╯╰───╯╰───╯╰───╯╰───╯╰───────╯
#
# The game is played by two players who sit opposite each other. Each player has a smaller one
# dimples on its side and a bigger dimple on the right - we call this bigger dimple
# by the player's «bank». At the beginning of the game, it is predetermined in each minor hole
# number of balls (this is the second parameter of the game), the banks are empty. The game is in progress
# in rounds, with players taking turns. The course of each round is as follows:
#
# • The player chooses one of his smaller holes that contains some
#   balls. If all of a player's holes are empty, the game ends (see below).
# • The player takes all the balls from the selected hole and starts them one at a time
#   divide into the following pits counterclockwise, inclusive
#   to your pot, but «not to the opponent's pot».
#   If, for example, the bottom player took the marbles from hole C, then they will be in sequence
#   divide into wells D, E, F, G, H, I, J, K, L, M, A, B, C, etc., until
#   he will have some marbles left.
# • If the last ball fell into an empty smaller hole during distribution
#   on the current player's side «and his opponent has some in the opposite hole
#   marbles", the player collects his last marble and "all" marbles, moves them to his bank.
# • If the last marble fell into the player's bank during the distribution, in the next
#   round is played by the same player again; otherwise, players take turns.
#
# ‹init› function returns a pair of lists representing the board with the ‹size› smaller holes 
# it is in at the beginning ‹start› balls. Both players' banks are empty. 

def init(size: int, start: int) -> tuple[list[int], list[int]]:
    list_a = []
    list_b = []
    for i in range(size):
        list_a.append(start)
        list_b.append(start)
    list_a.append(0)
    list_b.append(0)
    return (list_a, list_b)

# ‹play› procedure that plays one round of the game. Parameter ‹our› is a list representing 
# the current player's side, parameter ‹their› is a list representing the opponent's side. Assume that these lists
# have the same length greater than 1 and that they contain only non-negative integers.
# The ‹position› (integer) parameter specifies which dimple to select (0 is leftmost dimples from the player's point of view).

INVALID_POSITION = 0
EMPTY_POSITION = 1
ROUND_OVER = 2
PLAY_AGAIN = 3

def play(our, their, position):
    if (0 > position) or (position >= len(our) - 1): return INVALID_POSITION
    if our[position] == 0: return EMPTY_POSITION
    count = our[position]
    our[position] = 0
    position += 1
    while count > 0:
        for i in range(position, len(our)):
            if count == 1 and our[i] == 0 and (len(our) - 1) != i:
                our[len(our) - 1] += their[i] + 1
                their[i] = 0  
                return ROUND_OVER
            if count > 0:
                our[i] += 1
                if i == (len(our) - 1) and count == 1: return PLAY_AGAIN
                count -= 1
            else: continue
        position = 0
        for j in range(len(their) - 2, -1, -1):
            if count > 0:
                their[j] += 1
                count -= 1
            else: continue
    return ROUND_OVER    

def main():
    # --- init ---

    assert init(6, 3) \
        == ([3, 3, 3, 3, 3, 3, 0], [3, 3, 3, 3, 3, 3, 0])

    assert init(9, 7) \
        == ([7, 7, 7, 7, 7, 7, 7, 7, 7, 0], [7, 7, 7, 7, 7, 7, 7, 7, 7, 0])

    # --- play ---

    our = [3, 0, 6, 0]
    their = [3, 3, 3, 0]
    assert play(our, their, -1) == INVALID_POSITION
    assert our == [3, 0, 6, 0]
    assert their == [3, 3, 3, 0]

    our = [3, 0, 6, 0]
    their = [3, 3, 3, 0]
    assert play(our, their, 0) == PLAY_AGAIN
    assert our == [0, 1, 7, 1]
    assert their == [3, 3, 3, 0]

    our = [3, 0, 6, 0]
    their = [3, 3, 3, 0]
    assert play(our, their, 1) == EMPTY_POSITION
    assert our == [3, 0, 6, 0]
    assert their == [3, 3, 3, 0]

    our = [3, 0, 6, 0]
    their = [3, 3, 3, 0]
    assert play(our, their, 2) == ROUND_OVER
    assert our == [4, 0, 0, 6]
    assert their == [4, 0, 4, 0]

    our = [3, 0, 6, 0]
    their = [3, 3, 3, 0]
    assert play(our, their, 3) == INVALID_POSITION
    assert our == [3, 0, 6, 0]
    assert their == [3, 3, 3, 0]


if __name__ == '__main__':
    main()
