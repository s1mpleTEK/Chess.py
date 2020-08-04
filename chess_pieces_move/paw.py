#!/usr/bin/python3

def paw_move(table, user, src, dest):
    if table[src[1]][src[2]] == table[dest[1]][dest[2]]:
        print("you must move")
        return (False)
    if user[2] == 1:
        if src[1] == 7:
            if dest[1] == src[1]-1 or dest[1] == src[1]-2 and dest[2] == src[2]:
                return (True)
        elif dest[1] == src[1]-1 and dest[2] == src[2]:
            return (True)
        else:
            print("you can not move here")
    elif user[2] == 2:
        if src[1] == 2:
            if dest[1] == src[1]+1 or dest[1] == src[1]+2 and dest[2] == src[2]:
                return (True)
        elif dest[1] == src[1]+1 and dest[2] == src[2]:
            return (True)
        else:
            print("you can not move here")
    return (False)