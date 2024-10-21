def remove(my_list: list, *arg: int) -> list:
    if type(my_list) != list or type(arg[0]) != int: 
        raise Exception("Parameter given does not match variable type.")
    elif len(arg)>=3: raise Exception("Too many parameters given.")

    # last.append(my_list.copy())
    print(arg)
    if len(arg) == 1:
        my_list.pop(arg[0])

    elif len(arg) == 2:
        bruh = arg[1]+1
        del my_list[arg[0]:bruh]
    return my_list

def replace(my_list: list, arg: any, arg2:any) -> list:
    if type(my_list) != list: 
        raise Exception("Parameter given does not match variable type.")
    # last.append(my_list.copy())
    if type(arg) is list:
        if set(arg).issubset(set(my_list)):
            my_list[0:len(arg)] = arg2
    elif type(arg) is int:
        if arg in my_list:
            rep = my_list.index(arg)
            my_list[rep] = arg2
    else: 
        raise Exception("Sorry, arguments must be either int or a list.")
    
    return my_list

def test_remove():
    assert remove([1, 2, 3, 4], 2) == [1, 2, 4], "Should return [1, 2, 4] after removing index 2"
    assert remove([10, 20, 30, 40, 50], 1, 3) == [10, 50], "Should return [10, 50] after removing the slice"
    assert remove([5, 6, 7], 2) == [5, 6], "Should return [5, 6] after removing the last element"

def test_replace():
    assert replace([1, 2, 3], 2, 4) == [1, 4, 3], "Should return [1, 4, 3] after replacing 2 with 4"
    assert replace([1, 2, 3], [1, 2], [7, 8]) == [7, 8, 3], "Should return [7, 8, 3] after replacing [1, 2]"
    assert replace([1, 2, 3], 5, 9) == [1, 2, 3], "Should return [1, 2, 3] since 5 is not in the list"

