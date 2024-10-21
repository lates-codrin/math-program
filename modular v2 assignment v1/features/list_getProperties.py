import math
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
