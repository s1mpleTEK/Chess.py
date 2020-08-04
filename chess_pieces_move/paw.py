#!/usr/bin/python3

def paw_move(table, user, src, dest):                           #paw'script movement
    if table[src[1]][src[2]] == table[dest[1]][dest[2]]:        #verify if the player write the same source and destination for his chess piece
        print("you must move")
        return (False)
    if user[2] == 1:
        if src[1] == 7:                                         #verify if the paw is at its start line
            if dest[1] == src[1]-1 or dest[1] == src[1]-2:      #verify if the destionation is 1 or 2 more areas than at the start
                if dest[2] == src[2]:                           #verify if the column of the destination is the same with the source
                    return (True)
        elif dest[1] == src[1]-1 and dest[2] == src[2]:         #verify if the destionation is 1 more areas than at the start and in the same column that the source
            return (True)
    elif user[2] == 2:
        if src[1] == 2:                                         #verify if the paw is at its start line
            if dest[1] == src[1]+1 or dest[1] == src[1]+2:      #verify if the destionation is 1 or 2 more areas than at the start
                if dest[2] == src[2]:                           #verify if the column of the destination is the same with the source
                    return (True)
        elif dest[1] == src[1]+1 and dest[2] == src[2]:         #verify if the destionation is 1 more areas than at the start and in the same column that the source
            return (True)
    print("you can not move here")
    return (False)