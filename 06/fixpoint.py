from ib111 import week_06  # noqa

# A function ‹f› that, for a given integer ‹a›, returns a set
# containing ‹a›, ‹a // 2›, and ‹a // 7›. By applying this function to
# a set, we mean applying it to each element of the set and
# then combining all the results obtained.

# A function that applies ‹f› to the set from its argument
# will continue to apply ‹f› to the result obtained, and so on,
# until it reaches a point where further applications of ‹f› will no longer change the set
# . The result will be the number of applications of ‹f› to the set,
# which needed to be performed before the process stopped.

# For example, the first application of the described
# function to the set ‹{1, 5, 6}› produces the set ‹{0, 1, 2, 3, 5, 6}›:
#
# • the value ‹1› appears at ‹{1, 1 // 2 = 0, 1 // 7 = 0}›,
# • the value ‹5› at ‹{5, 5 // 2 = 2, 5 // 7 = 0}›, and finally
# • the value ‹6› at ‹{6, 6 // 2 = 3, 6 // 7 = 0}›.
#
# After the next application, the set does not change in any way, so the result is
# the number one.

def f(a: int) -> set[int]:
    return {a, a // 2, a // 7}

def fixpoint(starting_set: set[int]) -> int:
    final_set: set[int] = starting_set.copy()
    count: int = 0
    
    while True:
        new_set = set()
        for num in final_set:
            new_set.update(f(num))
        
        if new_set == final_set:
            break
        
        final_set = new_set
        count += 1
    
    return count

def main() -> None: # tests
    assert fixpoint({1, 5, 6}) == 1
    assert fixpoint({0, 1}) == 0
    assert fixpoint(set()) == 0
    assert fixpoint({8, 13, 7}) == 2
    assert fixpoint({13, 17, 29}) == 2
    assert fixpoint({13, 47}) == 4


if __name__ == '__main__':
    main()
