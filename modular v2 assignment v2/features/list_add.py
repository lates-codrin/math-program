def add(my_list: list, value: int)->list:
    if type(my_list) != list or type(value) != int: raise Exception("Parameter given does not match variable type.")
    # last.append(my_list.copy())
    my_list.append(value)
    return my_list

def insert(my_list : list, index: int, value: int)->list:
    if type(my_list) != list or type(value) != int or type(index) != int: raise Exception("Parameter given does not match variable type.")

    # last.append(my_list.copy())
    my_list.insert(index, value)
    return my_list

def test_add():
    assert add([0,1,2,3], 10) == [0,1,2,3,10], "Function test_add() did not output correctly"
    assert add([], 100) == [100], "Function test_add() did not output correctly"
    assert add([10], 100) ==[10,100], "Function test_add() did not output correctly"
def test_insert():
    assert insert([9,7,6,5], 1, 8) == [9,8,7,6,5], "Function test_insert() did not output correctly"
    assert insert([],0,1) == [1], "Function test_insert() did not output correctly"
    assert insert([100,101,102],0,99) == [99,100,101,102], "Function test_insert() did not output correctly"
    assert insert([999,998,997],3,996) == [999,998,997,996], "Function test_insert() did not output correctly"
test_insert()
test_add()