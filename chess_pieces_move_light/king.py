#!/usr/bin/python3

def king_move(table, user, src, dest, pieces, empty_space):         #king's movements script
    calc_y = int(dest[1]-src[1])                                    #calcul if the queen goes up or down
    calc_x = int(dest[2]-src[2])                                    #calcul if the queen goes right or left

    if table[src[1]][src[2]] == table[dest[1]][dest[2]]:            #verify if the player write the same source and destination for his chess piece
        print("you must move")
        return (False)

    if user[2] == 1:
        if table[dest[1]][dest[2]] in pieces[1]:                    #verify that the player can't move on his chess pieces
            print("you can not move here")
            return (False)
    elif user[2] == 2:
        if table[dest[1]][dest[2]] in pieces[0]:                    #verify that the player can't move on his chess pieces
            print("you can not move here")
            return (False)

    for i in range (1,2):                                           #browse the line and column and diagonal
        if calc_x == 0:                                             #if king stays in same column
            if calc_y > 0:                                          #if king goes down
                if src[1]+i == dest[1] and src[2] == dest[2]:       #⭣
                    return (True)
                elif table[src[1]+i][src[2]] != empty_space:        #verify if the path is clear
                    print("you can not move here")
                    return (False)
            if calc_y < 0:                                          #if king goes up
                if src[1]-i == dest[1] and src[2] == dest[2]:       #⭡
                    return (True)
                elif table[src[1]-i][src[2]] != empty_space:        #verify if the path is clear
                    print("you can not move here")
                    return (False)
        if calc_y == 0:                                             #if king stays in same line
            if calc_x > 0:                                          #if king goes right
                if src[1] == dest[1] and src[2]+i == dest[2]:       #⭢
                    return (True)
                elif table[src[1]][src[2]+i] != empty_space:        #verify if the path is clear
                    print("you can not move here")
                    return (False)
            if calc_x < 0:                                          #if king goes left
                if src[1] == dest[1] and src[2]-i == dest[2]:       #⭠
                    return (True)
                elif table[src[1]][src[2]-i] != empty_space:        #verify if the path is clear
                    print("you can not move here")
                    return (False)
        if calc_y > 0:                                              #if king goes down
            if calc_x > 0:                                          #if king goes right
                if src[1]+i == dest[1] and src[2]+i == dest[2]:     #⭨
                    return (True)
                elif table[src[1]+i][src[2]+i] != empty_space:      #verify if the path is clear
                    print("you can not move here")
                    return (False)
            if calc_x < 0:                                          #if king goes left
                if src[1]+i == dest[1] and src[2]-i == dest[2]:     #⭩
                    return (True)
                elif table[src[1]+i][src[2]-i] != empty_space:      #verify if the path is clear
                    print("you can not move here")
                    return (False)
        if calc_y < 0:                                              #if king goes up
            if calc_x > 0:                                          #if king goes right
                if src[1]-i == dest[1] and src[2]+i == dest[2]:     #⭧
                    return (True)
                elif table[src[1]-i][src[2]+i] != empty_space:      #verify if the path is clear
                    print("you can not move here")
                    return (False)
            if calc_x < 0:                                          #if king goes left
                if src[1]-i == dest[1] and src[2]-i == dest[2]:     #⭦
                    return (True)
                elif table[src[1]-i][src[2]-i] != empty_space:      #verify if the path is clear
                    print("you can not move here")
                    return (False)

    print("you can not move here")
    return (False)