def undo(v: list, last: list)->list:
    v.clear()
    v.extend(last[-1])
    del(last[-1])
    return v

# work in progress

def test_undo():
    # let the first parameter be the list after an operation has been applied to it
    # and the second parameter be the queue containing the original list(s)
    v = [1, 2, 3, 4]
    last = [[1, 2, 3]]
    assert undo(v, last) == [1, 2, 3], "Should undo and return [1, 2, 3]"

    # undo multiple times
    v = [50, 60, 70]
    last = [[5, 15, 25], [10, 20, 30], [20, 40, 60], [30, 50, 70]]  # 4 previous lists

    assert undo(v, last) == [30, 50, 70], "Should undo to [30, 50, 70] after one undo"
    assert undo(v, last) == [20, 40, 60], "Should undo to [20, 40, 60] after two undos"
    assert undo(v, last) == [10, 20, 30], "Should undo to [10, 20, 30] after three undos"
    assert undo(v, last) == [5, 15, 25], "Should undo to [5, 15, 25] after four undos"


    # undo when theres only 1 thing to undo
    v = [100]
    last = [[200]]  # Only one previous state
    assert undo(v, last) == [200], "Should undo to [200]"

    v=[]
    last=[[1]]
    assert undo(v,last) == [1], "No modifications so nothing to undo"

test_undo()
