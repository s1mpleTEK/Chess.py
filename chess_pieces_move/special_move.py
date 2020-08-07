#!/usr/bin/python3

def castling_move(table, user, src, dest, empty_space):
    if user[2] == 1:
        if dest[1] == 8:
            if dest[2] == 1:
                for i in range (2, 5):
                    if table[8][i] != empty_space:
                        return (False)
            elif dest[2] == 8:
                for i in range (6,8):
                    if table[8][i] != empty_space:
                        return (False)
    elif user[2] == 2:
        if dest[1] == 1:
            if dest[2] == 1:
                for i in range (2, 5):
                    if table[1][i] != empty_space:
                        return (False)
            elif dest[2] == 8:
                for i in range (6,8):
                    if table[1][i] != empty_space:
                        return (False)
    return (True)