from ib111 import week_03

# a pure function that has only a single number as input and output, but uses a list for its calculation.
# Calculation of the nth element of a sequence.
# We will use sequence:
#  ⟦ a₁ = 1
#    aₙ = ∑ₖ₌₁ⁿ⁻¹ d(k,n)⋅aₖ ⟧
#
# where ⟦d(k,n) = k⟧ when ⟦k⟧ divides ⟦n⟧ and 0 else.

def sequence(position):
    seq = [1]

    while len(seq) < position:
        # ‹n› contains index of current number (starting from 1).
        n = len(seq) + 1
        total = 0
        k = 1
        # Calculation of the sum
        while k < n:
            if n % k == 0:
                total += k * seq[k - 1]
            k += 1

        seq.append(total)

    return seq[position - 1]

def main():  # demo
    from_oeis = [1, 1, 1, 3, 1, 6, 1, 15, 4, 8, 1, 54, 1, 10, 9,
                 135, 1, 78, 1, 100, 11, 14, 1, 822, 6, 16, 40]
    for i in range(len(from_oeis)):
        assert sequence(i + 1) == from_oeis[i]


if __name__ == '__main__':
    main()
