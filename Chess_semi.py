#!/usr/bin/python3

import numpy as np
import re

from chess_pieces_move_semi.paw import paw_move, paw_evolution
from chess_pieces_move_semi.knight import knight_move
from chess_pieces_move_semi.bishop import bishop_move
from chess_pieces_move_semi.rook import rook_move
from chess_pieces_move_semi.queen import queen_move
from chess_pieces_move_semi.king import king_move
from chess_pieces_move_semi.special_move import castling_move

empty_space = "_"
corner = "¤"
pieces =    [[u"\u2659", u"\u2658", u"\u2657", u"\u2656", u"\u2655", u"\u2654"],        #pawn, knight, bishop, rook, queen, king (white)
            [u"\u265F", u"\u265E", u"\u265D", u"\u265C", u"\u265B", u"\u265A"]]         #pawn, knight, bishop, rook, queen, king (black)
area =      [["A", "B", "C", "D", "E", "F", "G", "H"],                                  #x axis
            [1, 2, 3, 4, 5, 6, 7, 8]]                                                   #y axis
castling = [0, 0]                                                                       #player 2, player 1
rooks_move = [[0, 0], [0, 0]]                                                           #player 2: left rook, right rook/player 1: left rook, right rook
kings_move = [0, 0]                                                                     #player 2: king/player 1: king

def set_user():                                         #set name for players
    user =   [input("Player 1 enter your name: "),      #name of player 1
            input("Player 2 enter your name: "),        #name of player 2
            1]                                          #player turn: 1 means O & 2 means X & 0 means someone win & -1 means tie

    return (user)

def set_table():                                    #init game board
    table = np.zeros((9,10), dtype=str)            #init empty list 10x10 ([9][9])
    for i in range (9):                           #set * in every line
        table[i] = empty_space

    for i in range (2):                             #i=0 > i=1
        table[8] = corner                         #set ¤ in every corner and browse y of table (first line and last line)
        for j in range (1,9):                       #browse x of table
            table[8][j] = area[0][j-1]            #A>B>C>D>E>F>G>H
        for j in range (8):                       #browse y of table and set the number 8 to 1 at [1][0] to [8][0] and [1][9] to [8][9]
            table[j][i*9] = area[1][-(j+1)]       #1>2>3>4>5>6>7>8

    return (set_pieces(table))

def set_pieces(table):                                              #set all pieces on the board
    for j in range (1,3):                                           #j equal 1 and 2 // set white pieces when j=1 and set black pieces when j=2
        # for i in range (1, 9):                                      #i equal 1 to 8 // when j=1 edit line[2] and when j=2 edit line[7]
        #         table[j**j+j*(j-1)][i] = pieces[j-1][0]           #set pawns
        for i in range (1,3):                                       #i equal 1 and 2 // when j=1 edit line[1] and when j=2 edit line[8]
                table[j**3-1][i**3] = pieces[j-1][3]                  #set rooks | i=1 -> i**3 = 1**3 = 1 / i=2 -> i**3 = 2**3 = 8
                # table[j**3-1][i**i+i*(i-1)+1] = pieces[j-1][1]        #set knights | i=1 -> i**i+i*(i-1)+1 = 1**1+1*(1-1)+1 = 1+1*0+1 = 2 / i=2 -> i**i+i*(i-1)+1 = 2**2+2*(2-1)+1 = 4+2*1+1 = 6+1 = 7
                # table[j**3-1][i*3] = pieces[j-1][2]                   #set bishops | i=1 -> i*3 = 1*3 = 3 / i=2 -> i*3 = 2*3 = 6
                # table[j**3-1][4] = pieces[j-1][4]                     #set queen
                table[j**3-1][5] = pieces[j-1][5]                     #set king

    return (table)

def alph_to_index(str):                 #convert alphabet to number for index
    for i in range (8):                 #0 to 7 for make A to H
        if ord(str) == ord("A")+i:      #check the good letter for find the good index
            return (i+1)

def verification_good_piece(table, user, src):      #verify that the player select their chess pieces
    if user[2] == 1:
        if table[src[1]][src[2]] in pieces[1]:      #verify that player 1 takes black chess pieces
            return (True)
    else:
        if table[src[1]][src[2]] in pieces[0]:      #verify that player 2 takes white chess pieces
            return (True)
    return (False)

def game_loop(table, user):                                                                 #interaction with player
    #choose chess piece
    src = [input("Select the area with the chess piece you want to play: "), "", ""]        #src[input player, table[line], table[column]]
    if len(src[0]) == 2 and bool(re.match('^[a-hA-H1-8]*$', src[0]))==True:                 #verify if src[input player] has length equal 2 and if it founds a-hA-H1-8 in this input
        for i in range (2):                                                                 #for browse src[input player]
            if bool(re.match('^[a-hA-H]*$', src[0][i]))==True:                              #for separate number and letter
                src[2] = alph_to_index(src[0][i].upper())                                   #put letter in src[table[column]]
            else:
                src[1] = 8 - int(src[0][i])                                                 #put number in src[table[line]]
        if table[src[1]][src[2]] == empty_space:                                            #verify if the player select empty space
            print("wrong area")
            return (game_loop(table, user))
        elif verification_good_piece(table, user, src) == False:                            #verify that the player select their chess pieces
            print("not your's")
            return (game_loop(table, user))
    else:                                                                                   #if the player write wrong information
        print("wrong input")
        return (game_loop(table, user))

    #choose destination of chess piece
    dest = [input("Select the area where you want to move the chess piece: "), "", ""]      #dest[input player, table[line], table[column]]
    if len(dest[0]) == 2 and bool(re.match('^[a-hA-H1-8]*$', dest[0]))==True:               #verify if dest[input player] has length equal 2 and if it founds a-hA-H1-8 in this input
        for i in range (2):                                                                 #for browse dest[input player]
            if bool(re.match('^[a-hA-H]*$', dest[0][i]))==True:                             #for separate number and letter
                dest[2] = alph_to_index(dest[0][i].upper())                                 #put letter in dest[table[column]]
            else:
                dest[1] = 8 - int(dest[0][i])                                               #put number in dest[table[line]]
    else:                                                                                   #if the player write wrong information
        print("wrong input")
        return (game_loop(table, user))
    return (detection_piece(table, user, src, dest))

def detection_piece(table, user, src, dest):                                        #detect the good chess piece
    for j in range (2):                                                             #for browse pieces[]
        if table[src[1]][src[2]] == pieces[j][0]:                                   #if chess piece equal paw
            if paw_move(table, user, src, dest, pieces, empty_space) == True:       #read paw's movements script
                return (move_pieces(table, user, src, dest))
        if table[src[1]][src[2]] == pieces[j][1]:                                   #if chess piece equal knight
            if knight_move(table, user, src, dest, pieces) == True:                 #read knignt's movements script
                return (move_pieces(table, user, src, dest))
        if table[src[1]][src[2]] == pieces[j][2]:                                   #if chess piece equal bishop
            if bishop_move(table, user, src, dest, pieces, empty_space) == True:    #read bishop's movements script
                return (move_pieces(table, user, src, dest))
        if table[src[1]][src[2]] == pieces[j][3]:                                   #if chess piece equal rook
            if rook_move(table, user, src, dest, pieces, empty_space) == True:      #read rook's movements script
                if src[1] == 7*j:                                                 #check if the src equal 1 or 8
                    if src[2] == 1:                                                 #check if src equal 1 for column
                        rooks_move[j][0] = 1                                        #add 1 if the left rook moves
                    elif src[2] == 8:                                               #check if src equal 8 for column
                        rooks_move[j][1] = 1                                        #add 1 if the right rook moves
                print(rooks_move)
                return (move_pieces(table, user, src, dest))
        if table[src[1]][src[2]] == pieces[j][4]:                                   #if chess piece equal queen
            if queen_move(table, user, src, dest, pieces, empty_space) == True:     #read queen's movements script
                return (move_pieces(table, user, src, dest))
        if table[src[1]][src[2]] == pieces[j][5]:                                   #if chess piece equal king
            if castling[j] == -1:
                print("you have already did a castling")
            elif table[dest[1]][dest[2]] == pieces[j][3] and castling[j] == 0 and\
            kings_move[j] == 0 and\
            castling_move(table, user, src, dest, empty_space, rooks_move) == True: #verify if the destination is a rook, the player has already did a castling and if the castling is legal
                castling[j] = 1                                                     #if castling equal 1 it means that the player did or has did a castling
                return (move_pieces(table, user, src, dest))
            elif castling[j] == 0 and kings_move[j] == 1\
            and table[dest[1]][dest[2]] == pieces[j][3]:                            #if the king's player has already moved and that the player did not of castling
                print("your king has already moved")
            if king_move(table, user, src, dest, pieces, empty_space) == True:      #read king's movements script
                kings_move[j] = 1                                                   #if kings_move equal 1 it means that the king has already moved
                return (move_pieces(table, user, src, dest))
    return (game_loop(table, user))

def move_pieces(table, user, src, dest):                                #update board and move chess piece
    if user[2] == 1:
        if table[src[1]][src[2]] == pieces[1][0] and dest[1] == 0:      #verify if the paw of player 1 moves on the last line for evolve
            table = paw_evolution(table, src, pieces[1])
        if castling[1] == 1:                                            #verify if the castling is on
            if dest[1] == 7:                                            #verify the line of the destination
                if dest[2] == 1:                                        #check the left rook for special movement (big castling/queenside)
                    tmp = table[dest[1]][dest[2]]                       #save the rook
                    table[dest[1]][dest[2]] = empty_space               #set an empty space at the destination (rook place/a1)
                    table[7][4] = tmp                                   #set the rook at is new place (d1)
                    table[7][3] = table[src[1]][src[2]]                 #set the king at new place (c1)
                    table[src[1]][src[2]] = empty_space                 #set an empty space at oldest place of the king
                elif dest[2] == 8:                                      #check the left rook for special movement (little castling/kingside)
                    tmp = table[dest[1]][dest[2]]                       #save the rook
                    table[dest[1]][dest[2]] = empty_space               #set an empty space at the destination (rook place/h1)
                    table[7][6] = tmp                                   #set the rook at is new place (f1)
                    table[7][7] = table[src[1]][src[2]]                 #set the king at new place (g1)
                    table[src[1]][src[2]] = empty_space                 #set an empty space at oldest place of the king
            castling[1] = -1                                            #set castling at -1 because the player 1 use their castling of the game
        elif table[dest[1]][dest[2]] == empty_space:                      #verify if the destination of the chess piece is empty
            table[dest[1]][dest[2]] = table[src[1]][src[2]]             #move the chess piece to their destination
            table[src[1]][src[2]] = empty_space                         #put a empty space at the source of the chess piece
        elif table[dest[1]][dest[2]] in pieces[0]:                      #verify if the destination of the chess piece is possessed by an opposent's chess piece
            table[dest[1]][dest[2]] = table[src[1]][src[2]]             #move the chess piece to thier destination
            table[src[1]][src[2]] = empty_space                         #put a empty space at the source of the chess piece
    elif user[2] == 2:
        if table[src[1]][src[2]] == pieces[0][0] and dest[1] == 7:      #verify if the paw of player 2 moves on the last line for evolve
            table = paw_evolution(table, src, pieces[0])
        if castling[0] == 1:
            if dest[1] == 0:
                if dest[2] == 1:                                        #check the left rook for special movement (big castling/queenside)
                    tmp = table[dest[1]][dest[2]]                       #save the rook
                    table[dest[1]][dest[2]] = empty_space               #set an empty space at the destination (rook place/a8)
                    table[0][4] = tmp                                   #set the rook at is new place (d8)
                    table[0][3] = table[src[1]][src[2]]                 #set the king at new place (c8)
                    table[src[1]][src[2]] = empty_space                 #set an empty space at oldest place of the king
                elif dest[2] == 8:                                      #check the left rook for special movement (little castling/kingside)
                    tmp = table[dest[1]][dest[2]]                       #save the rook
                    table[dest[1]][dest[2]] = empty_space               #set an empty space at the destination (rook place/h8)
                    table[0][6] = tmp                                   #set the rook at is new place (f8)
                    table[0][7] = table[src[1]][src[2]]                 #set the king at new place (g8)
                    table[src[1]][src[2]] = empty_space                 #set an empty space at oldest place of the king
            castling[0] = -1                                            #set castling at -1 because the player 2 use their castling of the game
        elif table[dest[1]][dest[2]] == empty_space:                      #verify if the destination of the chess piece is empty
            table[dest[1]][dest[2]] = table[src[1]][src[2]]             #move the chess piece to their destination
            table[src[1]][src[2]] = empty_space                         #put a empty space at the source of the chess piece
        elif table[dest[1]][dest[2]] in pieces[1]:                      #verify if the destination of the chess piece is possessed by an opposent's chess piece
            table[dest[1]][dest[2]] = table[src[1]][src[2]]             #move the chess piece to thier destination
            table[src[1]][src[2]] = empty_space                         #put a empty space at the source of the chess piece

    display_table(table)
    return (table)

def game_condition(table, user):
    if user[2] == 1:
        user[2] = 2
    else:
        user[2] = 1

    return (user)

def display_table(table):       #display game board
    print("")

    for i in range (9):
        print(table[i])

    print("")
    return

if __name__ == "__main__":
    try:
        user = set_user()                           #set name for player
        table = set_table()                         #init game board
        display_table(table)                        #display game board
        while (True):
            print(user[user[2]-1],"'s turn")
            table = game_loop(table, user)          #interaction with the player
            user = game_condition(table, user)      
            if user[2] == 0 or user[2] == -1:
                break
    except (EOFError, KeyboardInterrupt) as error:
        exit()