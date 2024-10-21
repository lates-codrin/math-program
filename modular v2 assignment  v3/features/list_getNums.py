import math
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
