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