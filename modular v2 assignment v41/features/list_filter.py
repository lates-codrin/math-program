from features.list_getNums import prime

def filter_prime(my_list: list) -> list:
    """Filters out non-prime numbers from a given list.

    Args:
        my_list (list): The list of integers to filter prime numbers from.

    Returns:
        list: A new list containing only the prime numbers from the original list.

    Raises:
        Exception: If an invalid list is passed.
    """
    if type(my_list) is not list: raise ValueError("Argument given is not a list.")
    length = len(my_list)
    toappend = prime(my_list, 0, length)
    my_list.clear()
    my_list = toappend
    return my_list

def filter_negative(my_list: list) -> list:
    """Filters out non-negative numbers from a given list.

    Args:
        my_list (list): The list of integers to filter negative numbers from.

    Returns:
        list: A new list containing only the negative numbers from the original list.

    Raises:
        Exception: If an invalid list is passed.
    """

    if type(my_list) is not list: raise ValueError("Argument given is not a list.")

    toappend = []
    for x in my_list:
        if x < 0:
            toappend.append(x)
    my_list.clear()
    my_list = toappend
    
    return my_list

def test_filter_prime():
    """Tests the filter_prime function to ensure it correctly filters prime numbers.

    Raises:
        AssertionError: If the filter_prime function does not return the expected results.
    """
    assert filter_prime([2, 3, 4, 5, 6, 7]) == [2, 3, 5, 7], "Should return only prime numbers [2, 3, 5, 7]"
    assert filter_prime([4, 6, 8, 10, 12]) == [], "Should return an empty list since there are no primes"
    assert filter_prime([11, 14, 17, 19, 20]) == [11, 17, 19], "Should return [11, 17, 19] as prime numbers"

def test_filter_negative():
    """Tests the filter_negative function to ensure it correctly filters negative numbers.

    Raises:
        AssertionError: If the filter_negative function does not return the expected results.
    """
    assert filter_negative([1, -2, 3, -4, 5]) == [-2, -4], "Should return [-2, -4]"
    assert filter_negative([1, 2, 3, 4, 5]) == [], "Should return an empty list"
    assert filter_negative([-1, -2, -3, -4]) == [-1, -2, -3, -4], "Should return the same list of negatives"
