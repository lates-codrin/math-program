def undo(my_list: list, last: list) -> list:
    """Reverts `my_list` to its previous state from the `last` list of states.

    Args:
        my_list (list): The current list to be reverted.
        last (list): The list storing previous states of `my_list`.

    Returns:
        list: The reverted list, `my_list`, after undoing the last change.
    """
    
    if type(my_list) is not list or type(last) is not list:
        raise TypeError("Arguments given are not lists.")
    if len(last) > 0:
        my_list.clear()
        my_list.extend(last[-1])
        del last[-1]
    return my_list

# work in progress

def test_undo():
    """Tests the `undo` function to ensure it correctly reverts to a previous state.

    Raises:
        AssertionError: If the undo function does not return the expected results.
    """
    v = [1, 2, 3, 4]
    last = [[1, 2, 3]]
    assert undo(v, last) == [1, 2, 3], "Should undo and return [1, 2, 3]"

    v = [50, 60, 70]
    last = [[5, 15, 25], [10, 20, 30], [20, 40, 60], [30, 50, 70]]  # Multiple undos
    assert undo(v, last) == [30, 50, 70], "Should undo to [30, 50, 70]"
    assert undo(v, last) == [20, 40, 60], "Should undo to [20, 40, 60]"
    assert undo(v, last) == [10, 20, 30], "Should undo to [10, 20, 30]"
    assert undo(v, last) == [5, 15, 25], "Should undo to [5, 15, 25]"

    v = [100]
    last = [[200]]
    assert undo(v, last) == [200], "Should undo to [200]"

    v = []
    last = [[1]]
    assert undo(v, last) == [1], "Should undo to [1]"
test_undo()
