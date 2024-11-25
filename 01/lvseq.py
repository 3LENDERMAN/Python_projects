from ib111 import week_01  # noqa

# Pure function ‹nth_element_lv› that returns the ‹index›th
# element of a sequence that is formed like this:
# ⟦ x₀ = 2
# x₁ = p
# xₙ = pxₙ₋₁ - qxₙ₋₂ ⟧

# Parameters ‹p›, ‹q› can be any integers, parameter
# ‹index› any non-negative integer

def nth_element_lv(p, q, index):
    xn_2 = 2
    xn_1 = p

    if index == 0: return xn_2
    if index == 1: return xn_1
    
    for i in range(index - 1):
        xn = (p * xn_1) - (q * xn_2)
        xn_2 = xn_1
        xn_1 = xn
            
    return xn


def main():
    assert nth_element_lv(7, 9, 0) == 2
    assert nth_element_lv(5, 4, 1) == 5
    assert nth_element_lv(1, -1, 5) == 11
    assert nth_element_lv(3, 2, 7) == 129


if __name__ == '__main__':
    main()
