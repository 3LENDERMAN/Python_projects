from ib111 import week_02  # noqa

# Function returns number ‹x›, which lies between values
# ‹low› and ‹high› (včetně), and for which function ‹poly› returns
# maximum value (⟦x⟧ for which all ⟦x'⟧ | ⟦f(x) ≥ f(x')⟧ where:
# ⟦f⟧ is function calculated by ‹poly›).

def poly(x):
    return 10 + 30 * x - 15 * x ** 3 + x ** 5

def maximum(low, high):
    max_x = low  
    max_value = poly(low) 
    
    for i in range(low, high + 1):
        current_value = poly(i)
        if current_value > max_value:
            max_value = current_value
            max_x = i 
            
    return max_x

def main(): # run tests
    assert maximum(0, 5) == 5
    assert maximum(0, 2) == 1
    assert maximum(-5, -1) == -3
    assert maximum(-2, 2) == -2
    assert maximum(-10, 10) == 10


if __name__ == "__main__":
    main()
