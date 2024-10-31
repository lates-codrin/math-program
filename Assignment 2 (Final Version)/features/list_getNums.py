from utils.is_prime import is_prime
def prime(my_list: list, index1: int, index2: int) -> list:
    """Returns all prime numbers from a sublist of `my_list`.

    Args:
        my_list (list): The list of integers from which prime numbers will be found.
        index1 (int): The starting index of the sublist.
        index2 (int): The ending index of the sublist.

    Returns:
        list: A list containing all prime numbers within the specified sublist.

    Raises:
        Exception: If invalid types or values are passed as arguments.

    Notes:
        - Uses a helper function `is_prime` to check if a number is prime.
    """
    primes = []

    if index1<0 or index1>index2 or index1 > len(my_list) or index2 > len(my_list): raise IndexError("Index cannot be negative or not in list.")

    for x in my_list[index1:index2]:
        if is_prime(x):
            primes.append(x)
    return primes

def odd(my_list: list, index1: int, index2: int) -> list:
    """Returns all even numbers from a sublist of `my_list`.

    Args:
        my_list (list): The list of integers from which even numbers will be filtered.
        index1 (int): The starting index of the sublist.
        index2 (int): The ending index of the sublist.

    Returns:
        list: A list containing all even numbers within the specified sublist.

    Raises:
        Exception: If invalid types or values are passed as arguments.

    Notes:
        - Uses a helper function `is_odd` to check if a number is even.
    """
    odds = []

    def is_odd(x: int) -> bool:
        """Determines if a number `x` is even.

        Args:
            x (int): The number to check for evenness.

        Returns:
            bool: True if `x` is even, False otherwise.
        """
        return x % 2 == 1

    if index1<0 or index1>index2 or index1 > len(my_list) or index2 > len(my_list): raise IndexError("Index cannot be negative or not in list.")

    for x in my_list[index1:index2]:
        if is_odd(x):
            odds.append(x)
    return odds


def test_prime():
    """Tests the `prime` function to ensure it correctly returns prime numbers.

    Raises:
        AssertionError: If the `prime` function does not return the expected results.
    """
    assert prime([2, 3, 5, 7, 9], 0, 5) == [2, 3, 5, 7], "Should return [2, 3, 5, 7]"
    assert prime([4, 6, 8, 10], 0, 4) == [], "Should return an empty list for no primes"
    assert prime([15, 17, 18, 19], 1, 3) == [17], "Should return [17] as the only prime in the range"

def test_odd():
    """Tests the `odd` function to ensure it correctly returns even numbers.

    Raises:
        AssertionError: If the `odd` function does not return the expected results.
    """
    assert odd([1, 2, 3, 4, 5], 0, 5) == [2, 4], "Should return [2, 4] as the even numbers"
    assert odd([1, 3, 5], 0, 3) == [], "Should return an empty list since all are odd"
    assert odd([10, 15, 20, 25], 0, 4) == [10, 20], "Should return [10, 20] as the even numbers"
