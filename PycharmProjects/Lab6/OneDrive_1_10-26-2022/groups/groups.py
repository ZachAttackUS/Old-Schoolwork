def groups_of_3(list):
    n = 3
    return ([list[i:i+n] for i in range(0, len(list), n)])
