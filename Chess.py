#!/usr/bin/python3

import numpy as np
import re
import os

from lib.pieces_move.paw import paw_move, paw_evolution
from lib.pieces_move.knight import knight_move
from lib.pieces_move.bishop import bishop_move
from lib.pieces_move.rook import rook_move
from lib.pieces_move.queen import queen_move
from lib.pieces_move.king import king_move
from lib.pieces_move.special_move import castling_move

from lib.chess_conditions.check_condition import check

from lib.game_history.history import History, Os

entity =        [[u"\u2659", u"\u2658", u"\u2657", u"\u2656", u"\u2655", u"\u2654"],        #pawn, knight, bishop, rook, queen, king (white) player 2
                [u"\u265F", u"\u265E", u"\u265D", u"\u265C", u"\u265B", u"\u265A"],         #pawn, knight, bishop, rook, queen, king (black) player 1
                ['_', "¤"]]                                                                 #empty_space, corner
area =          [["A", "B", "C", "D", "E", "F", "G", "H"],                                  #x axis
                [1, 2, 3, 4, 5, 6, 7, 8]]                                                   #y axis
castling =      [0, 0]                                                                      #player 2, player 1
rooks_move =    [[0, 0], [0, 0]]                                                            #player 2: left rook, right rook/player 1: left rook, right rook
kings_move =    [0, 0]                                                                      #player 2: king/player 1: king  
tech_check_status =  [0, 0, 0]                                                                      #player 1, player 2 / 1 means check before, 2 means check after and 3 means check mate
path_pieces =   [["","",""],                                                                #source of the pieces
                ["","",""]]                                                                 #destination of the pieces

def set_user():                                         #set name for players
    user =   [input("Player 1 enter your name: "),      #name of player 1
            input("Player 2 enter your name: "),        #name of player 2
            1,                                          #player turn: 1 means player 1 & 2 means player 2 & 0 means someone win & -1 means tie
            0]

    return (user)

def set_table():                                    #init game board
    table = np.zeros((10,10), dtype=str)            #init empty list 10x10 ([9][9])
    for i in range (1,9):                           #set _ in every line
        table[i] = entity[2][0]

    for i in range (2):                             #i=0 > i=1
        table[i*9] = entity[2][1]                         #set ¤ in every corner and browse y of table (first line and last line)
        for j in range (1,9):                       #browse x of table
            table[i*9][j] = area[0][j-1]            #A>B>C>D>E>F>G>H
        for j in range (1,9):                       #browse y of table and set the number 8 to 1 at [1][0] to [8][0] and [1][9] to [8][9]
            table[j][i*9] = area[1][-(j-1)-1]       #1>2>3>4>5>6>7>8

    return (set_pieces(table))

def set_tmp_table():                                    #init game board
    table = np.zeros((10,10), dtype=str)            #init empty list 10x10 ([9][9])
    for i in range (1,9):                           #set _ in every line
        table[i] = entity[2][0]

    for i in range (2):                             #i=0 > i=1
        table[i*9] = entity[2][1]                         #set ¤ in every corner and browse y of table (first line and last line)
        for j in range (1,9):                       #browse x of table
            table[i*9][j] = area[0][j-1]            #A>B>C>D>E>F>G>H
        for j in range (1,9):                       #browse y of table and set the number 8 to 1 at [1][0] to [8][0] and [1][9] to [8][9]
            table[j][i*9] = area[1][-(j-1)-1]       #1>2>3>4>5>6>7>8

    return (table)

def set_pieces(table):                                              #set all pieces on the board
    for j in range (1,3):                                           #j equal 1 and 2 // set white pieces when j=1 and set black pieces when j=2
        for i in range (1, 9):                                      #i equal 1 to 8 // when j=1 edit line[2] and when j=2 edit line[7]
                table[j**j+j*(j-1)+1][i] = entity[j-1][0]           #set pawns
        for i in range (1,3):                                       #i equal 1 and 2 // when j=1 edit line[1] and when j=2 edit line[8]
                table[j**3][i**3] = entity[j-1][3]                  #set rooks | i=1 -> i**3 = 1**3 = 1 / i=2 -> i**3 = 2**3 = 8
                table[j**3][i**i+i*(i-1)+1] = entity[j-1][1]        #set knights | i=1 -> i**i+i*(i-1)+1 = 1**1+1*(1-1)+1 = 1+1*0+1 = 2 / i=2 -> i**i+i*(i-1)+1 = 2**2+2*(2-1)+1 = 4+2*1+1 = 6+1 = 7
                table[j**3][i*3] = entity[j-1][2]                   #set bishops | i=1 -> i*3 = 1*3 = 3 / i=2 -> i*3 = 2*3 = 6
                table[j**3][4] = entity[j-1][4]                     #set queen
                table[j**3][5] = entity[j-1][5]                     #set king

    return (table)

def alph_to_index(str):                 #convert alphabet to number for index
    for i in range (8):                 #0 to 7 for make A to H
        if ord(str) == ord("A")+i:      #check the good letter for find the good index
            return (i+1)

def verification_good_piece(table, user):      #verify that the player select their chess pieces
    if user[2] == 1:
        if table[path_pieces[0][1]][path_pieces[0][2]] in entity[1]:      #verify that player 1 takes black chess pieces
            return (True)
    else:
        if table[path_pieces[0][1]][path_pieces[0][2]] in entity[0]:      #verify that player 2 takes white chess pieces
            return (True)
    return (False)

def game_loop(table, user):                                                                 #interaction with player
    #choose chess piece
    path_pieces[0][0] = input("Select the area with the chess piece you want to play: ")        #src[input player, table[line], table[column]]
    if len(path_pieces[0][0]) == 2 and bool(re.match('^[a-hA-H1-8]*$', path_pieces[0][0]))==True:                 #verify if src[input player] has length equal 2 and if it founds a-hA-H1-8 in this input
        for i in range (2):                                                                 #for browse src[input player]
            if bool(re.match('^[a-hA-H]*$', path_pieces[0][0][i]))==True:                              #for separate number and letter
                path_pieces[0][2] = alph_to_index(path_pieces[0][0][i].upper())                                   #put letter in src[table[column]]
            else:
                path_pieces[0][1] = 9 - int(path_pieces[0][0][i])                                                 #put number in src[table[line]]
        if table[path_pieces[0][1]][path_pieces[0][2]] == entity[2][0]:                                            #verify if the player select empty space
            print("wrong area")
            return (game_loop(table, user))
        elif verification_good_piece(table, user) == False:                            #verify that the player select their chess pieces
            print("not your's")
            return (game_loop(table, user))
    else:                                                                                   #if the player write wrong information
        print("wrong input")
        return (game_loop(table, user))

    #choose destination of chess piece
    path_pieces[1][0] = input("Select the area where you want to move the chess piece: ")      #dest[input player, table[line], table[column]]
    if len(path_pieces[1][0]) == 2 and bool(re.match('^[a-hA-H1-8]*$', path_pieces[1][0]))==True:               #verify if dest[input player] has length equal 2 and if it founds a-hA-H1-8 in this input
        for i in range (2):                                                                 #for browse dest[input player]
            if bool(re.match('^[a-hA-H]*$', path_pieces[1][0][i]))==True:                             #for separate number and letter
                path_pieces[1][2] = alph_to_index(path_pieces[1][0][i].upper())                                 #put letter in dest[table[column]]
            else:
                path_pieces[1][1] = 9 - int(path_pieces[1][0][i])                                               #put number in dest[table[line]]
    else:                                                                                   #if the player write wrong information
        print("wrong input")
        return (game_loop(table, user))
    return (detection_piece(table, user))

def detection_piece(table, user):                                        #detect the good chess piece
    for j in range (2):                                                             #for browse pieces[]
        if table[path_pieces[0][1]][path_pieces[0][2]] == entity[j][0]:                                   #if chess piece equal paw
            if paw_move(table, user, path_pieces, entity) == True:       #read paw's movements script
                return (move_pieces(table, user))
        if table[path_pieces[0][1]][path_pieces[0][2]] == entity[j][1]:                                   #if chess piece equal knight
            if knight_move(table, user, path_pieces, entity) == True:                 #read knignt's movements script
                return (move_pieces(table, user))
        if table[path_pieces[0][1]][path_pieces[0][2]] == entity[j][2]:                                   #if chess piece equal bishop
            if bishop_move(table, user, path_pieces, entity) == True:    #read bishop's movements script
                return (move_pieces(table, user))
        if table[path_pieces[0][1]][path_pieces[0][2]] == entity[j][3]:                                   #if chess piece equal rook
            if rook_move(table, user, path_pieces, entity) == True:      #read rook's movements script
                if path_pieces[0][1] == 7*j+1:                                                 #check if the src equal 1 or 8
                    if path_pieces[0][2] == 1:                                                 #check if src equal 1 for column
                        rooks_move[j][0] = 1                                        #add 1 if the left rook moves
                    elif path_pieces[0][2] == 8:                                               #check if src equal 8 for column
                        rooks_move[j][1] = 1                                        #add 1 if the right rook moves
                return (move_pieces(table, user))
        if table[path_pieces[0][1]][path_pieces[0][2]] == entity[j][4]:                                   #if chess piece equal queen
            if queen_move(table, user, path_pieces, entity) == True:     #read queen's movements script
                return (move_pieces(table, user))
        if table[path_pieces[0][1]][path_pieces[0][2]] == entity[j][5]:                                   #if chess piece equal king
            if table[path_pieces[1][1]][path_pieces[1][2]] == entity[j][3] and castling[j] == 0 and\
            kings_move[j] == 0 and\
            castling_move(table, user, path_pieces, entity, rooks_move) == True: #verify if the destination is a rook, the player has already did a castling and if the castling is legal
                castling[j] = 1                                                     #if castling equal 1 it means that the player did or has did a castling
                return (move_pieces(table, user))
            elif castling[j] == 0 and kings_move[j] == 1\
            and table[path_pieces[1][1]][path_pieces[1][2]] == entity[j][3]:                            #if the king's player has already moved and that the player did not of castling
                print("your king has already moved")
            elif castling[j] == -1 and table[path_pieces[1][1]][path_pieces[1][2]] == entity[j][3]:                            #if the king's player has already moved and that the player did not of castling
                print("you have already did a castling")
            if king_move(table, user, path_pieces, entity) == True:      #read king's movements script
                kings_move[j] = 1                                                   #if kings_move equal 1 it means that the king has already moved
                return (move_pieces(table, user))
    return (game_loop(table, user))

def move_pieces(table, user):                                #update board and move chess piece
    if user[2] == 1:
        if table[path_pieces[0][1]][path_pieces[0][2]] == entity[1][0] and path_pieces[1][1] == 1:      #verify if the paw of player 1 moves on the last line for evolve
            table = paw_evolution(table, path_pieces, entity[1])
        if castling[1] == 1:                                            #verify if the castling is on
            if path_pieces[1][1] == 8:                                            #verify the line of the destination
                if path_pieces[1][2] == 1:                                        #check the left rook for special movement (big castling/queenside)
                    tmp = table[path_pieces[1][1]][path_pieces[1][2]]                       #save the rook
                    table[path_pieces[1][1]][path_pieces[1][2]] = entity[2][0]               #set an empty space at the destination (rook place/a1)
                    table[8][4] = tmp                                   #set the rook at is new place (d1)
                    table[8][3] = table[path_pieces[0][1]][path_pieces[0][2]]                 #set the king at new place (c1)
                    table[path_pieces[0][1]][path_pieces[0][2]] = entity[2][0]                 #set an empty space at oldest place of the king
                elif path_pieces[1][2] == 8:                                      #check the left rook for special movement (little castling/kingside)
                    tmp = table[path_pieces[1][1]][path_pieces[1][2]]                       #save the rook
                    table[path_pieces[1][1]][path_pieces[1][2]] = entity[2][0]               #set an empty space at the destination (rook place/h1)
                    table[8][6] = tmp                                   #set the rook at is new place (f1)
                    table[8][7] = table[path_pieces[0][1]][path_pieces[0][2]]                 #set the king at new place (g1)
                    table[path_pieces[0][1]][path_pieces[0][2]] = entity[2][0]                 #set an empty space at oldest place of the king
            castling[1] = -1                                            #set castling at -1 because the player 1 use their castling of the game
        elif table[path_pieces[1][1]][path_pieces[1][2]] == entity[2][0]:                      #verify if the destination of the chess piece is empty
            table[path_pieces[1][1]][path_pieces[1][2]] = table[path_pieces[0][1]][path_pieces[0][2]]             #move the chess piece to their destination
            table[path_pieces[0][1]][path_pieces[0][2]] = entity[2][0]                         #put a empty space at the source of the chess piece
        elif table[path_pieces[1][1]][path_pieces[1][2]] in entity[0]:                      #verify if the destination of the chess piece is possessed by an opposent's chess piece
            table[path_pieces[1][1]][path_pieces[1][2]] = table[path_pieces[0][1]][path_pieces[0][2]]             #move the chess piece to thier destination
            table[path_pieces[0][1]][path_pieces[0][2]] = entity[2][0]                         #put a empty space at the source of the chess piece
    elif user[2] == 2:
        if table[path_pieces[0][1]][path_pieces[0][2]] == entity[0][0] and path_pieces[1][1] == 8:      #verify if the paw of player 2 moves on the last line for evolve
            table = paw_evolution(table, path_pieces, entity[0])
        if castling[0] == 1:
            if path_pieces[1][1] == 1:
                if path_pieces[1][2] == 1:                                        #check the left rook for special movement (big castling/queenside)
                    tmp = table[path_pieces[1][1]][path_pieces[1][2]]                       #save the rook
                    table[path_pieces[1][1]][path_pieces[1][2]] = entity[2][0]               #set an empty space at the destination (rook place/a8)
                    table[1][4] = tmp                                   #set the rook at is new place (d8)
                    table[1][3] = table[path_pieces[0][1]][path_pieces[0][2]]                 #set the king at new place (c8)
                    table[path_pieces[0][1]][path_pieces[0][2]] = entity[2][0]                 #set an empty space at oldest place of the king
                elif path_pieces[1][2] == 8:                                      #check the left rook for special movement (little castling/kingside)
                    tmp = table[path_pieces[1][1]][path_pieces[1][2]]                       #save the rook
                    table[path_pieces[1][1]][path_pieces[1][2]] = entity[2][0]               #set an empty space at the destination (rook place/h8)
                    table[1][6] = tmp                                   #set the rook at is new place (f8)
                    table[1][7] = table[path_pieces[0][1]][path_pieces[0][2]]                 #set the king at new place (g8)
                    table[path_pieces[0][1]][path_pieces[0][2]] = entity[2][0]                 #set an empty space at oldest place of the king
            castling[0] = -1                                            #set castling at -1 because the player 2 use their castling of the game
        elif table[path_pieces[1][1]][path_pieces[1][2]] == entity[2][0]:                    #verify if the destination of the chess piece is empty
            table[path_pieces[1][1]][path_pieces[1][2]] = table[path_pieces[0][1]][path_pieces[0][2]]             #move the chess piece to their destination
            table[path_pieces[0][1]][path_pieces[0][2]] = entity[2][0]                         #put a empty space at the source of the chess piece
        elif table[path_pieces[1][1]][path_pieces[1][2]] in entity[1]:                      #verify if the destination of the chess piece is possessed by an opposent's chess piece
            table[path_pieces[1][1]][path_pieces[1][2]] = table[path_pieces[0][1]][path_pieces[0][2]]             #move the chess piece to thier destination
            table[path_pieces[0][1]][path_pieces[0][2]] = entity[2][0]                         #put a empty space at the source of the chess piece

    return (table)

def game_condition(table, tmp_table, user):
    tech_check_status[user[2]-1] = check(table, tmp_table, user, entity)

    if user[2] == 1:
        if tech_check_status[0] == 0:
            user[3] = 1
            tech_check_status[2] = check(table, tmp_table, user, entity)
            if tech_check_status[2] == 2:
                print("The player", user[1],"is under check now")
            user[2] = 2
    elif user[2] == 2:
        if tech_check_status[1] == 0:
            user[3] = 1
            tech_check_status[2] = check(table, tmp_table, user, entity)
            if tech_check_status[2] == 2:
                print("The player", user[0],"is under check now")
            user[2] = 1

    user[3] = 0
    return (user)

def display_table(table):       #display game board
    print("")

    for i in range (10):
        print(table[i])

    print("")
    return

def load_table(table, tmp_table):
    for i in range (10):
        for j in range (10):
            tmp_table[i][j] = table[i][j]
    
    return (tmp_table)

if __name__ == "__main__":
    try:
        user = set_user()                           #set name for player
        Os(user).os_operation(user)
        table = set_table()                         #init game board
        tmp_table = set_tmp_table()
        display_table(table)                        #display game board
        while (True):
            if (tech_check_status[user[2]-1] == 0):
                print(user[user[2]-1],"'s turn")
                tmp_table = load_table(table, tmp_table)

            table = game_loop(table, user)          #interaction with the player
            user = game_condition(table, tmp_table, user)

            if (tech_check_status[user[2]-1] == 1):
                table = load_table(tmp_table, table)
                print("you can not do this move because you already are under check")
                if user[2] == 1:
                    if kings_move[1] == 1 and castling[1] == 0:
                        if tmp_table[path_pieces[0][1]][path_pieces[0][2]] == entity[1][5]:
                            if table[path_pieces[0][1]][path_pieces[0][2]] == entity[1][5]:
                                kings_move[1] = 0
                elif user[2] == 2:
                    if kings_move[0] == 1 and castling[0] == 0:
                        if tmp_table[path_pieces[0][1]][path_pieces[0][2]] == entity[0][5]:
                            if table[path_pieces[0][1]][path_pieces[0][2]] == entity[0][5]:
                                kings_move[0] = 0

            if (tech_check_status[user[2]-1] == 2):
                table = load_table(tmp_table, table)
                print("you can not do this move because you are going under check")
                if user[2] == 1:
                    if castling[1] == -1:
                        if path_pieces[0][1] == 8 and path_pieces[0][2] == 5 and tmp_table[path_pieces[0][1]][path_pieces[0][2]] == entity[1][5]:
                            if path_pieces[1][1] == 8 and path_pieces[1][2] == 1 and tmp_table[path_pieces[1][1]][path_pieces[1][2]] == entity[1][3]:
                                if table[8][3] != entity[1][5] and table[8][4] != entity[1][3]:
                                    castling[1] = 0
                            elif path_pieces[1][1] == 8 and path_pieces[1][2] == 8 and tmp_table[path_pieces[1][1]][path_pieces[1][2]] == entity[1][3]:
                                if table[8][7] != entity[1][5] and table[8][6] != entity[1][3]:
                                    castling[1] = 0
                elif user[2] == 2:
                    if castling[0] == -1:
                        if path_pieces[0][1] == 1 and path_pieces[0][2] == 5 and tmp_table[path_pieces[0][1]][path_pieces[0][2]] == entity[0][5]:
                            if path_pieces[1][1] == 1 and path_pieces[1][2] == 1 and tmp_table[path_pieces[1][1]][path_pieces[1][2]] == entity[0][3]:
                                if table[1][3] != entity[0][5] and table[1][4] != entity[0][3]:
                                    castling[0] = 0
                            elif path_pieces[1][1] == 1 and path_pieces[1][2] == 8 and tmp_table[path_pieces[1][1]][path_pieces[1][2]] == entity[0][3]:
                                if table[1][7] != entity[0][5] and table[1][6] != entity[0][3]:
                                    castling[0] = 0
            if tech_check_status[user[2]-1] == 0:
                History.history(table, tmp_table, path_pieces, entity, tech_check_status[2])

            if user[2] == 0 or user[2] == -1:
                break

            if (tech_check_status[user[2]-1] == 0):
                tmp_table = load_table(table, tmp_table)                       #save previous move
                display_table(table)
    except (EOFError, KeyboardInterrupt) as error:
        if os.path.exists(Os.path_file):
            os.close(History.file_history)
        exit()