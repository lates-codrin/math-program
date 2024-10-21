def add(my_list: list, value: int) -> list:
    """A function that appends a given value to a given list.

    Args:
        my_list (list): The list to which the value will be appended.
        value (int): The value to append to the list.

    Raises:
        Exception: If my_list is not a list or value is not an integer.

    Returns:
        list: The modified list after appending the value.
    """
    if type(my_list) != list or type(value) != int:
        raise Exception("Parameter given does not match variable type.")
    my_list.append(value)
    return my_list

def insert(my_list: list, index: int, value: int) -> list:
    """A function that inserts a value at a specific index in the given list.

    Args:
        my_list (list): The list in which the value will be inserted.
        index (int): The index where the value will be inserted.
        value (int): The value to insert at the given index.

    Raises:
        Exception: If my_list is not a list or index and value are not integers.

    Returns:
        list: The modified list after the value is inserted.
    """
    if type(my_list) != list or type(value) != int or type(index) != int:
        raise Exception("Parameter given does not match variable type.")
    if index<0 or index>len(my_list): raise IndexError("Index cannot be negative or not in list.")
    my_list.insert(index, value)
    return my_list

def test_add():
    """A function to test the correctness of the add() function.
    
    Raises:
        AssertionError: If the output from add() does not match the expected result.
    """
    assert add([0, 1, 2, 3], 10) == [0, 1, 2, 3, 10], "Function test_add() did not output correctly"
    assert add([], 100) == [100], "Function test_add() did not output correctly"
    assert add([10], 100) == [10, 100], "Function test_add() did not output correctly"

def test_insert():
    """A function to test the correctness of the insert() function.

    Raises:
        AssertionError: If the output from insert() does not match the expected result.
    """
    assert insert([9, 7, 6, 5], 1, 8) == [9, 8, 7, 6, 5], "Function test_insert() did not output correctly"
    assert insert([], 0, 1) == [1], "Function test_insert() did not output correctly"
    assert insert([100, 101, 102], 0, 99) == [99, 100, 101, 102], "Function test_insert() did not output correctly"
    assert insert([999, 998, 997], 3, 996) == [999, 998, 997, 996], "Function test_insert() did not output correctly"

test_insert()
test_add()
