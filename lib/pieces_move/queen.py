#!/usr/bin/python3

def queen_move(table, user, path_pieces, entity):        #queen's movements script
    calc_y = int(path_pieces[1][1]-path_pieces[0][1])                                    #calcul if the queen goes up or down
    calc_x = int(path_pieces[1][2]-path_pieces[0][2])                                    #calcul if the queen goes right or left

    if table[path_pieces[0][1]][path_pieces[0][2]] == table[path_pieces[1][1]][path_pieces[1][2]]:            #verify if the player write the same source and destination for his chess piece
        print("you must move")
        return (False)

    if user[2] == 1:
        if table[path_pieces[1][1]][path_pieces[1][2]] in entity[1]:                    #verify that the player can't move on his chess pieces
            print("you can not move here")
            return (False)
    elif user[2] == 2:
        if table[path_pieces[1][1]][path_pieces[1][2]] in entity[0]:                    #verify that the player can't move on his chess pieces
            print("you can not move here")
            return (False)

    for i in range (1,8):                                           #browse the line and column and diagonal
        if calc_x == 0:                                             #if queen stays in same column
            if calc_y > 0:                                          #if queen goes down
                if path_pieces[0][1]+i == path_pieces[1][1] and path_pieces[0][2] == path_pieces[1][2]:       #⭣
                    return (True)
                elif table[path_pieces[0][1]+i][path_pieces[0][2]] != entity[2][0]:        #verify if the path is clear
                    print("you can not move here")
                    return (False)
            if calc_y < 0:                                          #if queen goes up
                if path_pieces[0][1]-i == path_pieces[1][1] and path_pieces[0][2] == path_pieces[1][2]:       #⭡
                    return (True)
                elif table[path_pieces[0][1]-i][path_pieces[0][2]] != entity[2][0]:        #verify if the path is clear
                    print("you can not move here")
                    return (False)
        if calc_y == 0:                                             #if queen stays in same line
            if calc_x > 0:                                          #if queen goes right
                if path_pieces[0][1] == path_pieces[1][1] and path_pieces[0][2]+i == path_pieces[1][2]:       #⭢
                    return (True)
                elif table[path_pieces[0][1]][path_pieces[0][2]+i] != entity[2][0]:        #verify if the path is clear
                    print("you can not move here")
                    return (False)
            if calc_x < 0:                                          #if queen goes left
                if path_pieces[0][1] == path_pieces[1][1] and path_pieces[0][2]-i == path_pieces[1][2]:       #⭠
                    return (True)
                elif table[path_pieces[0][1]][path_pieces[0][2]-i] != entity[2][0]:        #verify if the path is clear
                    print("you can not move here")
                    return (False)
        if calc_y > 0:                                              #if queen goes down
            if calc_x > 0:                                          #if queen goes right
                if path_pieces[0][1]+i == path_pieces[1][1] and path_pieces[0][2]+i == path_pieces[1][2]:     #⭨
                    return (True)
                elif table[path_pieces[0][1]+i][path_pieces[0][2]+i] != entity[2][0]:      #verify if the path is clear
                    print("you can not move here")
                    return (False)
            if calc_x < 0:                                          #if queen goes left
                if path_pieces[0][1]+i == path_pieces[1][1] and path_pieces[0][2]-i == path_pieces[1][2]:     #⭩
                    return (True)
                elif table[path_pieces[0][1]+i][path_pieces[0][2]-i] != entity[2][0]:      #verify if the path is clear
                    print("you can not move here")
                    return (False)
        if calc_y < 0:                                              #if queen goes up
            if calc_x > 0:                                          #if queen goes right
                if path_pieces[0][1]-i == path_pieces[1][1] and path_pieces[0][2]+i == path_pieces[1][2]:     #⭧
                    return (True)
                elif table[path_pieces[0][1]-i][path_pieces[0][2]+i] != entity[2][0]:      #verify if the path is clear
                    print("you can not move here")
                    return (False)
            if calc_x < 0:                                          #if queen goes left
                if path_pieces[0][1]-i == path_pieces[1][1] and path_pieces[0][2]-i == path_pieces[1][2]:     #⭦
                    return (True)
                elif table[path_pieces[0][1]-i][path_pieces[0][2]-i] != entity[2][0]:      #verify if the path is clear
                    print("you can not move here")
                    return (False)

    print("you can not move here")
    return (False)