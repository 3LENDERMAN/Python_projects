from ib111 import week_02  # noqa
from math import sqrt, sin, cos, radians, acos, pi, isclose

# Function will calculate circuit of triangle always with different information provided: 
#   1. SSS three sides, 
#   2. SAS 2 sides and angle, 
#   3. ASA two angles and side.
#
#           ● A
#          ╱ ╲
#         ╱ α ╲
#        ╱     ╲
#     c ╱       ╲ b
#      ╱         ╲
#     ╱           ╲
#    ╱ β         γ ╲
# B ●───────────────● C
#           a

def perimeter_sss(a, b, c):
    return a + b + c

def perimeter_sas(a, gamma, b):
    c = sqrt(a ** 2 + b ** 2 - 2 * a * b * cos(radians(gamma)))
    return perimeter_sss(a, b, c)

def perimeter_asa(alpha, c, beta):
    gamma = radians(180 - alpha - beta)
    alpha = radians(alpha)
    beta = radians(beta)
    a = c * sin(alpha) / sin(gamma)
    b = c * sin(beta) / sin(gamma)
    return perimeter_sss(a, b, c)

def perimeter_aas(alpha, gamma, c):
    return perimeter_asa(alpha, c, 180 - alpha - gamma)

def get_alpha(a, b, c):
    return acos(float(b ** 2 + c ** 2 - a ** 2) /
                (2 * b * c)) * 180.0 / pi

def get_beta(a, b, c):
    return acos(float(a ** 2 + c ** 2 - b ** 2) /
                (2 * a * c)) * 180.0 / pi

# Helper procedure that works with basic triangle:
def check_triangle(a, b, c):
    alpha = get_alpha(a, b, c)
    beta = get_beta(a, b, c)
    gamma = 180 - alpha - beta

    assert isclose(perimeter_sss(a, b, c), a + b + c)
    assert isclose(perimeter_sas(a, gamma, b), a + b + c)
    assert isclose(perimeter_sas(b, alpha, c), a + b + c)
    assert isclose(perimeter_sas(c, beta, a), a + b + c)
    assert isclose(perimeter_asa(alpha, b, gamma), a + b + c)
    assert isclose(perimeter_asa(beta, a, gamma), a + b + c)
    assert isclose(perimeter_asa(alpha, c, beta), a + b + c)

def main():  # run tests
    for a in range(1, 6):
        for b in range(1, 6):
            for c in range(abs(a - b) + 1, a + b):
                check_triangle(a, b, c)

    alpha = get_alpha(3, 4, 5)
    beta = get_beta(3, 4, 5)
    assert isclose(perimeter_asa(alpha, 5, beta), 12)
    assert perimeter_asa(alpha, 5, beta) != 12
    assert perimeter_sas(3, 90, 4) == 12

if __name__ == '__main__':
    main()
