#!/usr/bin/python3

import numpy as np

empty_space = "_"
corner = "¤"
pieces =    [[u"\u2659", u"\u2658", u"\u2657", u"\u2656", u"\u2655", u"\u2654"],        #pawn, knight, bishop, rook, queen, king (white)
            [u"\u265F", u"\u265E", u"\u265D", u"\u265C", u"\u265B", u"\u265A"]]         #pawn, knight, bishop, rook, queen, king (black)

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
        for j in range (8):                         #browse x of table
            table[i*9][j+1] = chr(ord("A")+j)       #A>B>C>D>E>F>G>H

    for i in range (2):                             #browse x of table (first column and last column)
        for j in range (1,9):                       #browse y of table and set the number 8 to 1 at [1][0] to [8][0] and [1][9] to [8][9]
            table[j][i*9] = 9-j                     #1>2>3>4>5>6>7>8

    return (set_pieces(table))

def set_pieces(table):
    for j in range (2):                                     #browse to line 2 and line 7
        for i in range (1, 9):                              #browse to column 1 to column 8
            if j == 0:
                table[2][i] = pieces[0][0]                  #set white pawns
            elif j == 1:
                table[7][i] = pieces[1][0]                  #set black paws

    for j in range (2):                                     #browse to line 1 and 8
        for i in range (1,3):                               #i equal 1 and 2
            if j == 0:
                table[1][i**3] = pieces[0][3]               #set white rooks | i=1 -> i**3 = 1**3 = 1 / i=2 -> i**3 = 2**3 = 8
                table[1][i**i+i*(i-1)+1] = pieces[0][1]     #set white knights | i=1 -> i**i+i*(i-1)+1 = 1**1+1*(1-1)+1 = 1+1*0+1 = 2 / i=2 -> i**i+i*(i-1)+1 = 2**2+2*(2-1)+1 = 4+2*1+1 = 6+1 = 7
                table[1][i*3] = pieces[0][2]                #set white bishops | i=1 -> i*3 = 1*3 = 3 / i=2 -> i*3 = 2*3 = 6
            elif j == 1:
                table[8][i**3] = pieces[1][3]               #set black rooks | i=1 -> i**3 = 1**3 = 1 / i=2 -> i**3 = 2**3 = 8
                table[8][i**i+i*(i-1)+1] = pieces[1][1]     #set black knights | i=1 -> i**i+i*(i-1)+1 = 1**1+1*(1-1)+1 = 1+1*0+1 = 2 / i=2 -> i**i+i*(i-1)+1 = 2**2+2*(2-1)+1 = 4+2*1+1 = 6+1 = 7
                table[8][i*3] = pieces[1][2]                #set black bishops | i=1 -> i*3 = 1*3 = 3 / i=2 -> i*3 = 2*3 = 6

    for i in range (2):
        if i == 0:
            table[1][4] = pieces[0][4]                      #set white queen
            table[1][5] = pieces[0][5]                      #set white king
        elif i == 1:
            table[8][4] = pieces[1][4]                      #set black queen
            table[8][5] = pieces[1][5]                      #set black king

    return (table)

def game_loop(table, user):
    return (table)

def game_condition(table, user):
    return (user)

def display_table(table):       #display game board
    for i in range (10):
        print(table[i])

if __name__ == "__main__":
    try:
        user = set_user()       #set name for player
        table = set_table()     #init game board
        display_table(table)    #display game board
        # while (True):
        #     print(user[user[2]-1],"'s turn")
        #     table = game_loop(table, user)
        #     user = game_condition(table, user)
        #     if user[2] == 0 or user[2] == -1:
        #         break
    except (EOFError, KeyboardInterrupt) as error:
        exit()