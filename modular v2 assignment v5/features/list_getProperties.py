import math

def sum(my_list: list, index1: int, index2: int) -> int:
    """Calculates the sum of elements in a sublist from `my_list`.

    Args:
        my_list (list): The list of integers to sum.
        index1 (int): The starting index of the sublist.
        index2 (int): The ending index of the sublist.

    Returns:
        int: The sum of the elements in the sublist.
    """
    s = 0
    if index1<0 or index1>index2 or index1 > len(my_list) or index2 > len(my_list): raise IndexError("Index cannot be negative or not in list.")

    for x in my_list[index1:index2]:
        s += x
    return s

def gcd(my_list: list, index1: int, index2: int) -> int:
    """Calculates the GCD of all elements in a sublist from `my_list`.

    Args:
        my_list (list): The list of integers to calculate the GCD from.
        index1 (int): The starting index of the sublist.
        index2 (int): The ending index (exclusive) of the sublist.

    Returns:
        int: The GCD of the elements in the sublist.
    """
    if index1<0 or index1>index2 or index1 > len(my_list) or index2 > len(my_list): raise IndexError("Index cannot be negative or not in list.")
    s = my_list[index1]
    for x in my_list[index1:index2]:
        s = math.gcd(s, x)
    return s

def max(my_list: list, index1: int, index2: int) -> int:
    """Finds the maximum value in a sublist from `my_list`.

    Args:
        my_list (list): The list of integers to find the maximum value from.
        index1 (int): The starting index of the sublist.
        index2 (int): The ending index of the sublist.

    Returns:
        int: The maximum value in the sublist.
    """
    if index1<0 or index1>index2 or index1 > len(my_list) or index2 > len(my_list): raise IndexError("Index cannot be negative or not in list.")
    maxi = my_list[index1]
    for x in my_list[index1:index2]:
        maxi = max(x, maxi)
    return maxi

def test_sum():
    """
    Tests the `sum` function to ensure it correctly sums elements.
    
    Raises:
        AssertionError: If the sum function does not return the expected results.
    """
    assert sum([1, 2, 3, 4], 0, 4) == 10, "Should return the sum 10"
    assert sum([], 0, 0) == 0, "Should return 0 for an empty list"
    assert sum([-1, -2, -3], 0, 3) == -6, "Should return -6 for the sum of negative numbers"

def test_gcd():
    """Tests the `gcd` function to ensure it correctly calculates the GCD of elements.
    
    Raises:
        AssertionError: If the gcd function does not return the expected results.
    """
    assert gcd([12, 18, 24], 0, 3) == 6, "Should return GCD 6"
    assert gcd([5, 7, 11], 0, 3) == 1, "Should return GCD 1 for co-primes"
    assert gcd([9, 9, 9], 0, 3) == 9, "Should return 9 as all elements are the same"

def test_max():
    """Tests the `max` function to ensure it correctly identifies the maximum value.
    
    Raises:
        AssertionError: If the max function does not return the expected results.
    """
    assert max([1, 3, 5, 7], 0, 4) == 7, "Should return 7 as the maximum value"
    assert max([-1, -2, -3, -4], 0, 4) == -1, "Should return -1 as the maximum"
    assert max([42], 0, 1) == 42, "Should return 42 as the only element in the list"