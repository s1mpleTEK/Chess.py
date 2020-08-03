#!/usr/bin/python3

import numpy as np

def set_table():                                    #init game board
    table = np.zeros((10,10), dtype=str)            #init empty list 10x10 ([9][9])
    for i in range (1,9):                           #set * in every line
        table[i] = '*'

    for i in range (2):                             #i=0 > i=1
        table[i*9] = "¤"                            #set ¤ in every corner and browse y of table (first line and last line)
        for j in range (8):                         #browse x of table
            table[i*9][j+1] = chr(ord("A")+j)       #A>B>C>D>E>F>G>H

    for i in range (2):                             #browse x of table (first column and last column)
        for j in range (1,9):                       #browse y of table and set the number 8 to 1 at [1][0] to [8][0] and [1][9] to [8][9]
            table[j][i*9] = 9-j                     #1>2>3>4>5>6>7>8

    return (table)

def display_table(table):       #display game board
    for i in range (10):
        print(table[i])

if __name__ == "__main__":
    try:
        table = set_table()     #init game board
        display_table(table)    #display game board
    except (EOFError, KeyboardInterrupt) as error:
        exit()