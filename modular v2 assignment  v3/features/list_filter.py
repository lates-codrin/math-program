from features.list_getNums import prime

def filter_prime(my_list: list)->list:
    # last.append(my_list.copy())
    length = len(my_list)
    toappend = prime(my_list, 0, length)
    my_list.clear()
    my_list = toappend
    return my_list

def filter_negative(my_list: list)->list:
   #  last.append(my_list.copy())
    length = len(my_list)
    toappend = []
    for x in my_list:
        if x<0: toappend.append(x)
    my_list.clear()
    my_list = toappend
    return my_list
