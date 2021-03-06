def in2d(var, l):  # gets 2d list and checks whether var is in the list
    for item in l:
        for val in item:
            if val == var:
                return True
    return False


def index_in_2d(var, l):  # gets 2d list and returns index of var in list as tuple -1 if not found
    ind = ()
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] == var:
                ind = (i, j)
                return ind
    return -1


def find_key_in_dict_of_lists(dic, val):
    for i, j in zip(dic.keys(), dic.values()):
        if val in j:
            return i
    return False

