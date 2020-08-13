#!/usr/bin/python3

import re

def paw_move(table, user, path_pieces, entity):          #paw's movements script
    if table[path_pieces[0][1]][path_pieces[0][2]] == table[path_pieces[1][1]][path_pieces[1][2]]:            #verify if the player write the same source and destination for his chess piece
        print("you must move")
        return (False)

    if user[2] == 1:
        if table[path_pieces[1][1]][path_pieces[1][2]] in entity[1]:                    #verify that the player can't move on his chess pieces
            print("you can not move here")
            return (False)
        if table[path_pieces[1][1]][path_pieces[1][2]] == entity[2][0]:
            if path_pieces[0][1] == 6:                                         #verify if the paw is at its start line
                if path_pieces[1][1] == path_pieces[0][1]-1 or path_pieces[1][1] == path_pieces[0][1]-2:      #verify if the destionation is 1 or 2 more areas than at the start
                    if path_pieces[1][2] == path_pieces[0][2]:                           #verify if the column of the destination is the same with the source
                        return (True)
            elif path_pieces[1][1] == path_pieces[0][1]-1 and path_pieces[1][2] == path_pieces[0][2]:         #verify if the destionation is 1 more areas than at the start and in the same column that the source
                return (True)
        elif path_pieces[0][1]-1 == path_pieces[1][1]:                                   #verify if path_pieces[0][1]-1 equal path_pieces[1][1] for check if the paw moves 1by1 area
            if path_pieces[0][2]+1 == path_pieces[1][2]:                                 #verify if path_pieces[0][2]+1 (right) equal path_pieces[1][2] and if it is true the paw eats opposent's chess piece
                return (True)
            if path_pieces[0][2]-1 == path_pieces[1][2]:                                 #verify if path_pieces[0][2]-1 (left) equal path_pieces[1][2] and if it is true the paw eats opposent's chess piece
                return (True)
    elif user[2] == 2:
        if table[path_pieces[1][1]][path_pieces[1][2]] in entity[0]:                    #verify that the player can't move on his chess piece
            print("you can not move here")
            return (False)
        if table[path_pieces[1][1]][path_pieces[1][2]] == entity[2][0]:
            if path_pieces[0][1] == 1:                                         #verify if the paw is at its start line
                if path_pieces[1][1] == path_pieces[0][1]+1 or path_pieces[1][1] == path_pieces[0][1]+2:      #verify if the destionation is 1 or 2 more areas than at the start
                    if path_pieces[1][2] == path_pieces[0][2]:                           #verify if the column of the destination is the same with the source
                        return (True)
            elif path_pieces[1][1] == path_pieces[0][1]+1 and path_pieces[1][2] == path_pieces[0][2]:         #verify if the destionation is 1 more areas than at the start and in the same column that the source
                return (True)
        elif path_pieces[0][1]+1 == path_pieces[1][1]:                                   #verify if path_pieces[0][1]-1 equal path_pieces[1][1] for check if the paw moves 1by1 area
            if path_pieces[0][2]+1 == path_pieces[1][2]:                                 #verify if path_pieces[0][2]+1 (right) equal path_pieces[1][2] and if it is true the paw eats opposent's chess piece
                return (True)
            if path_pieces[0][2]-1 == path_pieces[1][2]:                                 #verify if path_pieces[0][2]-1 (left) equal path_pieces[1][2] and if it is true the paw eats opposent's chess piece
                return (True)

    print("you can not move here")
    return (False)

def paw_evolution(table, path_pieces, pieces):                                          #manage the evolution of paw
    print("Different upgrade:")                                                 #choice
    print("1 - Knight", pieces[1])                                              #knight
    print("2 - Bishop", pieces[2])                                              #bishop
    print("3 - Rook", pieces[3])                                                #rook
    print("4 - Queen", pieces[4])                                               #queen

    while True:
        upgrade = input("Choose one: ")                                         #intereact with the player
        if bool(re.match('^[1-4]*$', upgrade))==True and len(upgrade) == 1:     #verify if the player wrote a number between 1 and 4
            table[path_pieces[0][1]][path_pieces[0][2]] = pieces[int(upgrade)]                        #remplace the paw before it moves
            return (table)
        print("wrong input")                                                    #if the player wrote a wrong input, the loop don't break