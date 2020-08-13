#!/usr/bin/python3

def castling_move(table, user, path_pieces, empty_space, rooks_move):     #verification for validate castling
    if user[2] == 1:
        if path_pieces[1][1] == 8:                                                #verify the line of the destination
            if path_pieces[1][2] == 1 and rooks_move[1][0] == 0:                  #check the left rook and verify if it has already moved
                for i in range (2, 5):                                  #browse distance between king and rook at queenside
                    if table[8][i] != empty_space:                      #verify if the space between them it is empty
                        return (False)                                  #not empty
                    return (True)                                       #empty
            elif path_pieces[1][2] == 1 and rooks_move[1][0] != 0:                #if the rook has already moved
                print("this rook has already moved")
                return (False)
            if path_pieces[1][2] == 8 and rooks_move[1][1] == 0:                  #check the right rook and verify if it has already moved
                for i in range (6,8):                                   #browse distance between king and rook at kingside
                    if table[8][i] != empty_space:                      #verify if the space between them it is empty
                        return (False)                                  #not empty
                    return (True)                                       #empty
            elif path_pieces[1][2] == 8 and rooks_move[1][1] != 0:                #if the rook has already moved
                print("this rook has already moved")
                return (False)
    elif user[2] == 2:
        if path_pieces[1][1] == 1:                                                #verify the line of the destination
            if path_pieces[1][2] == 1 and rooks_move[0][0] == 0:                  #check the left rook and verify if it has already moved
                for i in range (2, 5):                                  #browse distance between king and rook at queenside
                    if table[1][i] != empty_space:                      #verify if the space between them it is empty
                        return (False)                                  #not empty
                    return (True)                                       #empty
            elif path_pieces[1][2] == 1 and rooks_move[0][0] != 0:                #if the rook has already moved
                print("this rook has already moved")
                return (False)
            if path_pieces[1][2] == 8 and rooks_move[0][1] == 0:                  #check the right rook and verify if it has already moved
                for i in range (6,8):                                   #browse distance between king and rook at kingside
                    if table[1][i] != empty_space:                      #verify if the space between them it is empty
                        return (False)                                  #not empty
                    return (True)                                       #empty
            elif path_pieces[1][2] == 8 and rooks_move[0][1] != 0:                #if the rook has already moved
                print("this rook has already moved")
                return (False)