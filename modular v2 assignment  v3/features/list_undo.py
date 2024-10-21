def undo(v: list, last: list)->list:
    v.clear()
    v.extend(last[-1])
    del(last[-1])
    return v

# work in progress