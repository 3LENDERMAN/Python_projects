from ib111 import week_03  # noqa


# Continued fraction takes list of coefficients and returns normal fraction
#
# ‹continued_fraction›, takes list of coefficients and returns fraction ‹(numerator, denominator)›.

def continued_fraction(coefficients):
    nom = 1
    denom = coefficients[len(coefficients) - 1]
    fraction = 0
    for coef in range(len(coefficients) - 1, 0, -1):
        fraction = coefficients[coef - 1] * denom + nom
        nom = denom
        denom = fraction
    return (denom, nom)

def main(): # run tests
    assert continued_fraction([4, 2, 6, 7]) == (415, 93)
    assert continued_fraction([3, 4, 12, 4]) == (649, 200)
    assert continued_fraction([0, 2, 4]) == (4, 9)


if __name__ == "__main__":
    main()
