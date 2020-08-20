#!/usr/bin/python3

import os
import datetime as dt

class History:
    hist = ""
    turn_player = 1
    turn_game = 1
    player1_move = ""
    player2_move = ""
    file_history = ""

class Os:
    path_dirs = "./game/"
    name_file = str(dt.datetime.now().date()) + "_"+ str(dt.datetime.now().time()) + ".txt"
    path_file = path_dirs + name_file

def history(table, tmp_table, path_pieces, entity):
    os_operation()
    if History.turn_player == 1:
        History.player1_move = str(path_pieces[0][0])+"-"+str(path_pieces[1][0])
        History.hist = History.player1_move
        os.write(History.file_history, str.encode(str(History.turn_game) + ". "))
        os.write(History.file_history, str.encode(History.hist + " "))
        History.turn_player = 2
    else:
        History.player2_move = str(path_pieces[0][0])+"-"+str(path_pieces[1][0])
        History.hist = History.player2_move
        History.turn_player = 1
        os.write(History.file_history, str.encode(History.hist))
        os.write(History.file_history, str.encode("\n"))
        History.turn_game = History.turn_game + 1
    return

def os_operation():
    if not os.path.exists(Os.path_dirs):
        os.makedirs(Os.path_dirs)
    if not os.path.exists(Os.path_file):
        History.file_history = os.open(Os.path_file, os.O_CREAT|os.O_RDWR)
    return