#!/usr/bin/python3

def knight_move(table, user, path_pieces, pieces):                #knight's movements script
    calc_y = int(path_pieces[1][1]-path_pieces[0][1])                                #calcul if the knight goes up or down
    calc_x = int(path_pieces[1][2]-path_pieces[0][2])                                #calcul if the knight goes right or left

    if table[path_pieces[0][1]][path_pieces[0][2]] == table[path_pieces[1][1]][path_pieces[1][2]]:        #verify if the player write the same source and destination for his chess piece
        print("you must move")
        return (False)

    if user[2] == 1:
        if table[path_pieces[1][1]][path_pieces[1][2]] in pieces[1]:                #verify that the player can't move on his chess pieces
            print("you can not move here")
            return (False)
    elif user[2] == 2:
        if table[path_pieces[1][1]][path_pieces[1][2]] in pieces[0]:                #verify that the player can't move on his chess pieces
            print("you can not move here")
            return (False)

    if calc_y > 0:                                              #if knight goes downn
        if calc_x > 0:                                          #if knght goes right
            if path_pieces[0][1]+2 == path_pieces[1][1] and path_pieces[0][2]+1 == path_pieces[1][2]:     #⮧
                return (True)
            if path_pieces[0][1]+1 == path_pieces[1][1] and path_pieces[0][2]+2 == path_pieces[1][2]:     #⮡
                return (True)
        if calc_x < 0:                                          #if knight goes left
            if path_pieces[0][1]+2 == path_pieces[1][1] and path_pieces[0][2]-1 == path_pieces[1][2]:     #⮦
                return (True)
            if path_pieces[0][1]+1 == path_pieces[1][1] and path_pieces[0][2]-2 == path_pieces[1][2]:     #⮠
                return (True)

    if calc_y < 0:                                              #if knight goes up
        if calc_x > 0:                                          #if knight goes right
            if path_pieces[0][1]-2 == path_pieces[1][1] and path_pieces[0][2]+1 == path_pieces[1][2]:     #⮥
                return (True)
            if path_pieces[0][1]-1 == path_pieces[1][1] and path_pieces[0][2]+2 == path_pieces[1][2]:     #⮣
                return (True)
        if calc_x < 0:                                          #if knight goes left
            if path_pieces[0][1]-2 == path_pieces[1][1] and path_pieces[0][2]-1 == path_pieces[1][2]:     #⮤
                return (True)
            if path_pieces[0][1]-1 == path_pieces[1][1] and path_pieces[0][2]-2 == path_pieces[1][2]:     #⮢
                return (True)

    print("you can not move here")
    return (False)