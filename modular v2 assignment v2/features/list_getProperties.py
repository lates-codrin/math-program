from utils import math
def sum(my_list: list, index1: int, index2: int)->int:
    s = 0

    for x in my_list[index1:index2]:
        s = s + x
    return s

def gcd(my_list: list, index1: int, index2: int)->int:
    s = my_list[index1]

    for x in my_list[index1:index2]:
        s = math.gcd(s,x)
    return s


def max(my_list: list, index1: int, index2: int)->int:
    maxi = my_list[index1]

    for x in my_list[index1:index2]:
        maxi = max(x,maxi)
    return maxi

def test_sum():
    assert sum([1, 2, 3, 4], 0, 4) == 10, "Should return the sum 10"
    assert sum([], 0, 0) == 0, "Should return 0 for an empty list"
    assert sum([-1, -2, -3], 0, 3) == -6, "Should return -6 for the sum of negative numbers"

def test_gcd():
    assert gcd([12, 18, 24], 0, 3) == 6, "Should return GCD 6"
    assert gcd([5, 7, 11], 0, 3) == 1, "Should return GCD 1 for co-primes"
    assert gcd([9, 9, 9], 0, 3) == 9, "Should return 9 as all elements are the same"

def test_max():
    assert max([1, 3, 5, 7], 0, 4) == 7, "Should return 7 as the maximum value"
    assert max([-1, -2, -3, -4], 0, 4) == -1, "Should return -1 as the maximum"
    assert max([42], 0, 1) == 42, "Should return 42 as the only element in the list"
