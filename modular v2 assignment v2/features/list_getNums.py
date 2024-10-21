from utils import math
def prime(my_list: list, index1: int, index2: int)->list:
    primes = []
    def is_prime(x:int)->bool:
        if x==2: return 1
        elif x<2 or x%2==0: return 0
        else:
            for d in range(3,math.isqrt(x),2):
                if x%d == 0: return 0
        return 1
    for x in my_list[index1:index2]:
        if is_prime(x): primes.append(x)
    return primes

def odd(my_list: list, index1: int, index2: int)->list:
    odds = []
    def is_odd(x:int)->bool:
        return x%2 == 0
    for x in my_list[index1:index2]:
        if is_odd(x): odds.append(x)
    return odds

def test_prime():
    assert prime([2, 3, 5, 7, 9], 0, 5) == [2, 3, 5, 7], "Should return [2, 3, 5, 7]"
    assert prime([4, 6, 8, 10], 0, 4) == [], "Should return an empty list for no primes"
    assert prime([15, 17, 18, 19], 1, 3) == [17], "Should return [17] as the only prime in the range"

def test_odd():
    assert odd([1, 2, 3, 4, 5], 0, 5) == [2, 4], "Should return [2, 4] as the even numbers"
    assert odd([1, 3, 5], 0, 3) == [], "Should return an empty list since all are odd"
    assert odd([10, 15, 20, 25], 0, 4) == [10, 20], "Should return [10, 20] as the even numbers"


