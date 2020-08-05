#!/usr/bin/python3

def knight_move(table, user, src, dest, pieces):                #knight's movements script
    calc_y = int(dest[1]-src[1])                                #calcul if the knight goes up or down
    calc_x = int(dest[2]-src[2])                                #calcul if the knight goes right or left

    if table[src[1]][src[2]] == table[dest[1]][dest[2]]:        #verify if the player write the same source and destination for his chess piece
        print("you must move")
        return (False)

    if user[2] == 1:
        if table[dest[1]][dest[2]] in pieces[1]:                #verify that the player can't move on his chess pieces
            print("you can not move here")
            return (False)
    elif user[2] == 2:
        if table[dest[1]][dest[2]] in pieces[0]:                #verify that the player can't move on his chess pieces
            print("you can not move here")
            return (False)

    if calc_y > 0:                                              #if knight goes downn
        if calc_x > 0:                                          #if knght goes right
            if src[1]+2 == dest[1] and src[2]+1 == dest[2]:     #⮧
                return (True)
            if src[1]+1 == dest[1] and src[2]+2 == dest[2]:     #⮡
                return (True)
        if calc_x < 0:                                          #if knight goes left
            if src[1]+2 == dest[1] and src[2]-1 == dest[2]:     #⮦
                return (True)
            if src[1]+1 == dest[1] and src[2]-2 == dest[2]:     #⮠
                return (True)

    if calc_y < 0:                                              #if knight goes up
        if calc_x > 0:                                          #if knight goes right
            if src[1]-2 == dest[1] and src[2]+1 == dest[2]:     #⮥
                return (True)
            if src[1]-1 == dest[1] and src[2]+2 == dest[2]:     #⮣
                return (True)
        if calc_x < 0:                                          #if knight goes left
            if src[1]-2 == dest[1] and src[2]-1 == dest[2]:     #⮤
                return (True)
            if src[1]-1 == dest[1] and src[2]-2 == dest[2]:     #⮢
                return (True)

    print("you can not move here")
    return (False)