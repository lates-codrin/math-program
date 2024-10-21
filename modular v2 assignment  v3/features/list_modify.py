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