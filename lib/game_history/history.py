#!/usr/bin/python3

import os
import sys
import datetime as dt

class History:
    hist = []
    turn = 1
    player1_move = ""
    player2_move = ""
    file_history = ""

class Os:
    path_dirs = "./game/"
    name_file = str(dt.datetime.now().date()) + "_"+ str(dt.datetime.now().time()) + ".txt"
    path_file = path_dirs + name_file

def history(table, tmp_table, path_pieces, entity):
    os_operation()
    if History.turn == 1:
        History.player1_move = str(path_pieces[0][0])+"-"+str(path_pieces[1][0])
        History.turn = 2
    else:
        History.player2_move = str(path_pieces[0][0])+"-"+str(path_pieces[1][0])
        History.hist.append([History.player1_move, History.player2_move])
        History.turn = 1
    return

def os_operation():
    if not os.path.exists(Os.path_dirs):
        os.makedirs(Os.path_dirs)
    if not os.path.exists(Os.path_file):
        History.file_history = os.open(Os.path_file, os.O_CREAT|os.O_APPEND)
    return