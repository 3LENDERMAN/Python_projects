from ib111 import week_02  # noqa

# <continued_fraction> finds value of ‹index› coefficient 
# in chain fragment for rational numerator ‹nom› denominator ‹denom›.

# For example chain fragment ⟦4 + (1 / (2 + 1 / (6 + (1/7))))⟧
# represents number ⟦415/93⟧ and coefficients are 4, 2, 6 and 7.

def continued_fraction(nom, denom, index):
    for i in range(index + 1):
        coef = nom // denom
        fraction = nom - (denom * coef)
        nom = denom
        denom = fraction
    return coef

def main(): # run tests
    assert continued_fraction(2, 1, 0) == 2
    assert continued_fraction(415, 93, 0) == 4
    assert continued_fraction(415, 93, 1) == 2
    assert continued_fraction(415, 93, 2) == 6
    assert continued_fraction(415, 93, 3) == 7
    assert continued_fraction(649, 200, 1) == 4
    assert continued_fraction(649, 200, 2) == 12
    assert continued_fraction(649, 200, 3) == 4
    assert continued_fraction(649, 200, 0) == 3
    assert continued_fraction(649, 200, 1) == 4
    assert continued_fraction(649, 200, 2) == 12
    assert continued_fraction(649, 200, 3) == 4
    assert continued_fraction(9, 4, 1) == 4
    assert continued_fraction(688, 219, 0) == 3
    assert continued_fraction(688, 219, 1) == 7
    assert continued_fraction(688, 219, 2) == 15
    assert continued_fraction(688, 219, 3) == 2


if __name__ == "__main__":
    main()
