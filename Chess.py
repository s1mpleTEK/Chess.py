#!/usr/bin/python3

import numpy as np

def set_table():
    table = np.zeros((8,8), dtype=str)
    for i in range (8):
        for j in range (8):
            table[i][j] = '.'
    return (table)

def display_table(table):
    for i in range (8):
        print(table[i])

if __name__ == "__main__":
    try:
        print("Hello word")
        table = set_table()
        display_table(table)
    except (EOFError, KeyboardInterrupt) as error:
        exit()