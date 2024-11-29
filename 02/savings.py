from ib111 import week_02  # noqa

# ‹savings_years› calculates for how many years ‹savings› will last, while:
# 1. Bank will add ‹interest_rate› at the end of the year (in percentiges)
# 2. At the beginning of each each, we withdraw ‹withdraw› amount
# 3. Each year ‹inflation› raises (constantly in percentages)

# Example: with 100000,- of savings, yearly withdraws 42000,-, 
# interest rate 3,2 % and inflation 1,5 %:
# first year: ⟦(100000 - 42000)⋅1.032 = 59856⟧ next ⟦42000⋅1.015⟧ = 42630...

def savings_years(savings, interest_rate, inflation, withdraw):
    years = 0
    while True:
        if withdraw > savings:
            return years
        savings -= withdraw
        years += 1
        withdraw *= 1 + inflation / 100
        savings += savings * (interest_rate / 100)

def main(): # run tests
    assert savings_years(1000, 0.0, 0.0, 100) == 10
    assert savings_years(1000, 5.0, 0.0, 100) == 13
    assert savings_years(1000, 6.0, 2.0, 100) == 12
    assert savings_years(100000, 3.2, 1.5, 42000) == 2
    assert savings_years(500000, 0.5, 3.7, 12000) == 26
    assert savings_years(2000000, 5.2, 2.5, 57000) == 88


if __name__ == "__main__":
    main()
