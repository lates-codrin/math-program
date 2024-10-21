def remove(my_list: list, *arg: int) -> list:
    """Removes elements from `my_list` based on the provided indices.

    Args:
        my_list (list): The list from which elements will be removed.
        *arg (int): Either a single index to remove one element, or two indices to remove a slice.

    Returns:
        list: The modified list after removing the specified element(s).

    Raises:
        Exception: If the provided arguments do not match the expected types or format.
    """
    if type(my_list) != list or type(arg[0]) != int:
        raise TypeError("Parameter given cannot be handled.")
    elif len(arg) >= 3:
        raise TypeError("Too many parameters given.")

    if len(arg) == 1:
        my_list.pop(arg[0])
    elif len(arg) == 2:
        bruh = arg[1] + 1
        del my_list[arg[0]:bruh]
    return my_list

def replace(my_list: list, arg: any, arg2: any) -> list:
    """Replaces occurrences of a value or sublist in `my_list` with another value or sublist.

    Args:
        my_list (list): The list to perform replacements on.
        arg (any): The value or sublist to be replaced.
        arg2 (any): The replacement value or sublist.

    Returns:
        list: The modified list after replacements.

    Raises:
        Exception: If the arguments do not match the expected types or cases.
    """
    if type(my_list) is not list:
        raise Exception("Parameter given does not match variable type.")

    # replace sublist with int
    if type(arg) is list and type(arg2) is int:
        i = 0
        while i <= len(my_list) - len(arg):
            if my_list[i:i + len(arg)] == arg:
                my_list[i:i + len(arg)] = [arg2]
                i += 1
            else:
                i += 1

    # replace int with list
    elif type(arg) is int and type(arg2) is list:
        i = 0
        while i < len(my_list):
            if my_list[i] == arg:
                my_list[i:i + 1] = arg2
                i += len(arg2)
            else:
                i += 1

    # replace int with int
    elif type(arg) is int and type(arg2) is int:
        my_list = [arg2 if x == arg else x for x in my_list]

    # replace sublist with list
    elif type(arg) is list and type(arg2) is list:
        i = 0
        while i <= len(my_list) - len(arg):
            if my_list[i:i + len(arg)] == arg:
                my_list[i:i + len(arg)] = arg2
                i += len(arg2)
            else:
                i += 1

    else:
        raise Exception("Sorry, something wrong happened.")
    
    return my_list


def test_remove():
    """Tests the `remove` function to ensure it correctly removes elements.
    
    Raises:
        AssertionError: If the remove function does not return the expected results.
    """
    assert remove([1, 2, 3, 4], 2) == [1, 2, 4], "Should return [1, 2, 4] after removing index 2"
    assert remove([10, 20, 30, 40, 50], 1, 3) == [10, 50], "Should return [10, 50] after removing the slice"
    assert remove([5, 6, 7], 2) == [5, 6], "Should return [5, 6] after removing the last element"

def test_replace():
    """Tests the `replace` function to ensure it correctly replaces values.
    
    Raises:
        AssertionError: If the replace function does not return the expected results.
    """
    assert replace([1, 2, 3], 2, 4) == [1, 4, 3], "Should return [1, 4, 3] after replacing 2 with 4"
    assert replace([1, 2, 3], [1, 2], [7, 8]) == [7, 8, 3], "Should return [7, 8, 3] after replacing [1, 2]"
    assert replace([1, 2, 3], 5, 9) == [1, 2, 3], "Should return [1, 2, 3] since 5 is not in the list"
    assert replace([1, 2, 3], [2], [3]) == [1, 3, 3], "Should replace [2] with [3]"
    assert replace([1, 2, 3], [1], [3]) == [3, 2, 3], "Should replace [1] with [3]"
    assert replace([1, 2, 3, 2, 4], 2, 8) == [1, 8, 3, 8, 4], "Should replace 2 with 8"



