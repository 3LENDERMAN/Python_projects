from ib111 import week_02  # noqa

# Consider eleven base representation ⟦0, 1, 2, 3, 4, 5, 6, 7, 8, 9⟧ + ⟦δ⟧ as 10
# Number is palindrome if in eleven-base we remove all ⟦δ⟧ and number is symmetrical

# Predicate returns True for valid palindrome, False otherwise

# Example: ⟦144⟧ is palindrome_z, in eleven-base: ⟦(121)ₑ⟧ or
# ⟦2564 = (1δ21)ₑ⟧, ⟦1211 = (δ01)ₑ⟧ a ⟦33670 = (2332δ)ₑ⟧...
# Non palindromes are: ⟦233 = (1δ2)ₑ⟧, ⟦1729 = (1332)ₑ⟧...

def elf_palindrome(num):
    normal = 0
    reversed_num = 0
    power = 1  
    
    while num > 0:
        remainder = num % 11
        
        if remainder != 10:
            normal = normal * 10 + remainder 
            reversed_num = reversed_num + remainder * power 
            power *= 10  

        num //= 11
    if normal % 10 == 0:
        normal //= 10
    return normal == reversed_num

def main() -> None: #run tests
    assert elf_palindrome(120)
    assert elf_palindrome(144)
    assert elf_palindrome(2564)
    assert elf_palindrome(1211)
    assert not elf_palindrome(233)
    assert not elf_palindrome(1729)


if __name__ == '__main__':
    main()
