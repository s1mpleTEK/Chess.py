#!/usr/bin/python3

import numpy as np
import re

empty_space = "_"
corner = "¤"
pieces =    [[u"\u2659", u"\u2658", u"\u2657", u"\u2656", u"\u2655", u"\u2654"],        #pawn, knight, bishop, rook, queen, king (white)
            [u"\u265F", u"\u265E", u"\u265D", u"\u265C", u"\u265B", u"\u265A"]]         #pawn, knight, bishop, rook, queen, king (black)
area =      [["A", "B", "C", "D", "E", "F", "G", "H"],
            [1, 2, 3, 4, 5, 6, 7, 8]]

def set_user():                                         #set name for players
    user =   [input("Player 1 enter your name: "),      #name of player 1
            input("Player 2 enter your name: "),        #name of player 2
            1]                                          #player turn: 1 means O & 2 means X & 0 means someone win & -1 means tie

    return (user)

def set_table():                                    #init game board
    table = np.zeros((10,10), dtype=str)            #init empty list 10x10 ([9][9])
    for i in range (1,9):                           #set * in every line
        table[i] = empty_space

    for i in range (2):                             #i=0 > i=1
        table[i*9] = corner                         #set ¤ in every corner and browse y of table (first line and last line)
        for j in range (1,9):                       #browse x of table
            table[i*9][j] = area[0][j-1]            #A>B>C>D>E>F>G>H
        for j in range (1,9):                       #browse y of table and set the number 8 to 1 at [1][0] to [8][0] and [1][9] to [8][9]
            table[j][i*9] = area[1][-(j-1)-1]                     #1>2>3>4>5>6>7>8

    return (set_pieces(table))

def set_pieces(table):                                              #set all pieces on the board
    for j in range (1,3):                                           #j equal 1 and 2 // set white pieces when j=1 and set black pieces when j=2
        for i in range (1, 9):                                      #i equal 1 to 8 // when j=1 edit line[2] and when j=2 edit line[7]
                table[j**j+j*(j-1)+1][i] = pieces[j-1][0]           #set pawns
        for i in range (1,3):                                       #i equal 1 and 2 // when j=1 edit line[1] and when j=2 edit line[8]
                table[j**3][i**3] = pieces[j-1][3]                  #set rooks | i=1 -> i**3 = 1**3 = 1 / i=2 -> i**3 = 2**3 = 8
                table[j**3][i**i+i*(i-1)+1] = pieces[j-1][1]        #set knights | i=1 -> i**i+i*(i-1)+1 = 1**1+1*(1-1)+1 = 1+1*0+1 = 2 / i=2 -> i**i+i*(i-1)+1 = 2**2+2*(2-1)+1 = 4+2*1+1 = 6+1 = 7
                table[j**3][i*3] = pieces[j-1][2]                   #set bishops | i=1 -> i*3 = 1*3 = 3 / i=2 -> i*3 = 2*3 = 6
                table[j**3][4] = pieces[j-1][4]                     #set queen
                table[j**3][5] = pieces[j-1][5]                     #set king

    return (table)

def alph_to_index(str):
    for i in range (8):
        if ord(str) == 65+i:
            return (i+1)

def verification_good_piece(table, user, src):
    if user[2] == 1:
        if table[src[1]][src[2]] in pieces[1]:
            return (True)
    else:
        if table[src[1]][src[2]] in pieces[0]:
            return (True)
    return (False)

def game_loop(table, user):
    src = [input("Select the area with the chess piece you want to play: "), "", ""]
    if len(src[0]) == 2 and bool(re.match('^[a-hA-H1-8]*$', src[0]))==True:
        for i in range (2):
            if bool(re.match('^[a-hA-H]*$', src[0][i]))==True:
                src[2] = alph_to_index(src[0][i].upper())
            else:
                src[1] = 9 - int(src[0][i])
        if verification_good_piece(table, user, src) == False:
            print("not your's")
            return (game_loop(table, user))
    else:
        print("wrong area")
        return(game_loop(table, user))

    dest = [input("Select the area where you want to move the chess piece: "), "", ""]
    if len(dest[0]) == 2 and bool(re.match('^[a-hA-H1-8]*$', dest[0]))==True:
        for i in range (2):
            if bool(re.match('^[a-hA-H]*$', dest[0][i]))==True:
                dest[2] = alph_to_index(dest[0][i].upper())
            else:
                dest[1] = 9 - int(dest[0][i])
    else:
        print("wrong area")
        return(game_loop(table, user))

    return (move_piece(table, user, src, dest))

def move_piece(table, user, src, dest):
    if user[2] == 1:
        if table[dest[1]][dest[2]] == empty_space:
            tmp = table[dest[1]][dest[2]]
            table[dest[1]][dest[2]] = table[src[1]][src[2]]
            table[src[1]][src[2]] = tmp
        elif table[dest[1]][dest[2]] in pieces[0]:
            table[dest[1]][dest[2]] = table[src[1]][src[2]]
            table[src[1]][src[2]] = empty_space
        else:
            print("you can't move here")
            return (game_loop(table, user))
    elif user[2] == 2:
        if table[dest[1]][dest[2]] == empty_space:
            tmp = table[dest[1]][dest[2]]
            table[dest[1]][dest[2]] = table[src[1]][src[2]]
            table[src[1]][src[2]] = tmp
        elif table[dest[1]][dest[2]] in pieces[1]:
            table[dest[1]][dest[2]] = table[src[1]][src[2]]
            table[src[1]][src[2]] = empty_space
        else:
            print("you can't move here")
            return (game_loop(table, user))

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

    for i in range (10):
        print(table[i])

    print("")

if __name__ == "__main__":
    try:
        user = set_user()       #set name for player
        table = set_table()     #init game board
        display_table(table)    #display game board
        while (True):
            print(user[user[2]-1],"'s turn")
            table = game_loop(table, user)
            user = game_condition(table, user)
            if user[2] == 0 or user[2] == -1:
                break
    except (EOFError, KeyboardInterrupt) as error:
        exit()