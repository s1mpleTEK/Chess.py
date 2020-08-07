#!/usr/bin/python3

import re

def paw_move(table, user, src, dest, pieces, empty_space):          #paw's movements script
    if table[src[1]][src[2]] == table[dest[1]][dest[2]]:            #verify if the player write the same source and destination for his chess piece
        print("you must move")
        return (False)

    if user[2] == 1:
        if table[dest[1]][dest[2]] in pieces[1]:                    #verify that the player can't move on his chess pieces
            print("you can not move here")
            return (False)
        if table[dest[1]][dest[2]] == empty_space:
            if src[1] == 6:                                         #verify if the paw is at its start line
                if dest[1] == src[1]-1 or dest[1] == src[1]-2:      #verify if the destionation is 1 or 2 more areas than at the start
                    if dest[2] == src[2]:                           #verify if the column of the destination is the same with the source
                        return (True)
            elif dest[1] == src[1]-1 and dest[2] == src[2]:         #verify if the destionation is 1 more areas than at the start and in the same column that the source
                return (True)
        elif src[1]-1 == dest[1]:                                   #verify if src[1]-1 equal dest[1] for check if the paw moves 1by1 area
            if src[2]+1 == dest[2]:                                 #verify if src[2]+1 (right) equal dest[2] and if it is true the paw eats opposent's chess piece
                return (True)
            if src[2]-1 == dest[2]:                                 #verify if src[2]-1 (left) equal dest[2] and if it is true the paw eats opposent's chess piece
                return (True)
    elif user[2] == 2:
        if table[dest[1]][dest[2]] in pieces[0]:                    #verify that the player can't move on his chess piece
            print("you can not move here")
            return (False)
        if table[dest[1]][dest[2]] == empty_space:
            if src[1] == 1:                                         #verify if the paw is at its start line
                if dest[1] == src[1]+1 or dest[1] == src[1]+2:      #verify if the destionation is 1 or 2 more areas than at the start
                    if dest[2] == src[2]:                           #verify if the column of the destination is the same with the source
                        return (True)
            elif dest[1] == src[1]+1 and dest[2] == src[2]:         #verify if the destionation is 1 more areas than at the start and in the same column that the source
                return (True)
        elif src[1]+1 == dest[1]:                                   #verify if src[1]-1 equal dest[1] for check if the paw moves 1by1 area
            if src[2]+1 == dest[2]:                                 #verify if src[2]+1 (right) equal dest[2] and if it is true the paw eats opposent's chess piece
                return (True)
            if src[2]-1 == dest[2]:                                 #verify if src[2]-1 (left) equal dest[2] and if it is true the paw eats opposent's chess piece
                return (True)

    print("you can not move here")
    return (False)

def paw_evolution(table, src, pieces):                                          #manage the evolution of paw
    print("Different upgrade:")                                                 #choice
    print("1 - Knight", pieces[1])                                              #knight
    print("2 - Bishop", pieces[2])                                              #bishop
    print("3 - Rook", pieces[3])                                                #rook
    print("4 - Queen", pieces[4])                                               #queen

    while True:
        upgrade = input("Choose one: ")                                         #intereact with the player
        if bool(re.match('^[1-4]*$', upgrade))==True and len(upgrade) == 1:     #verify if the player wrote a number between 1 and 4
            table[src[1]][src[2]] = pieces[int(upgrade)]                        #remplace the paw before it moves
            return (table)
        print("wrong input")                                                    #if the player wrote a wrong input, the loop don't break