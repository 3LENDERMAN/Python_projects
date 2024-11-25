from ib111 import week_03  # noqa

# «FreeCell» is a solitaire card game. It is used in the game
# a classic deck of 52 cards with four suits and thirteen values
# (ranks) from ace to king. 

# The playing field contains:
# • free fields (cells) – typically four, in variants one to ten,
# • home field (foundations) - always exactly four, into each of them
# they lay down cards of the same suit, successively from ace to king,
# • columns (cascades) – typically eight, in variants four to ten;
# all cards are dealt to the columns at the beginning.

# Card is a pair ‹(rank, suit)›, where rank is one of the numbers 1 to 13 
# and suit is one of the numbers 0 through 3 (representing successively
# hearts, diamonds, spades and clubs; again represented by constants below).
# Do not change the constants listed here.

ACE, JACK, QUEEN, KING = 1, 11, 12, 13
HEARTS, DIAMONDS, CLUBS, SPADES = 0, 1, 2, 3

# Implement the ‹can_move› predicate, i.e. if possible in the given situation
# move some card.
# • ‹cascades› is a list of column bottom tabs (‹None› is an empty column),
# • ‹cells› is a list of cards in free fields (‹None› is an empty field),
# • ‹foundation› is a list of top cards in home fields (‹None› is again an empty field).

def can_move(cascades, cells, foundation):
    # attempt to move from free position to column:
    for i in range(len(cells)):
        is_black = 1
        is_red = 1
        val, sym = cells[i]
        for j in range(len(cascades)):
            v, s = cascades[j]
            if s > 1: is_red = 0
            if sym < 2: is_black = 0
            if (val + 1) == v and is_black == is_red:
                return True
    # attempt to move from column to house:
    for i in range(len(cascades)):
        v, s = cascades[i]

        for j in range(len(foundation)):
            if foundation[j] == None:
                if v == 1: return True
                return False
            val, sym = foundation[j]
            if (v - 1) == val:
                return True
    # attempt to move from column to another column:
    for i in range(len(cascades)):
        v,s = cascades[i]
        is_black = 1
        is_red = 1
        for j in range(len(cascades)):
            val, sym = cascades[j]
            if s > 1: is_red = 0
            if sym < 2: is_black = 0
            if i != j and (v + 1) == val and s != sym:
                return True
    return False

def main():
    cascades = [(2, HEARTS), (3, HEARTS), (7, CLUBS), (8, CLUBS)]
    cells = [(2, CLUBS), (3, CLUBS), (4, CLUBS)]
    foundations = [None, None, None, None]
    assert can_move(cascades, cells, foundations)

    cells = [(2, DIAMONDS), (3, DIAMONDS), (4, DIAMONDS)]
    assert not can_move(cascades, cells, foundations)

    cells = [(2, DIAMONDS), (4, SPADES), (3, HEARTS)]
    assert not can_move(cascades, cells, foundations)

if __name__ == '__main__':
    main()
