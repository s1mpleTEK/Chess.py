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

def history(table, tmp_table, path_pieces, entity, check):
    os_operation()
    move_player = get_move_player(table, tmp_table, path_pieces, entity, check)
    if History.turn_player == 1:
        History.player1_move = move_player
        History.hist = History.player1_move
        os.write(History.file_history, str.encode(str(History.turn_game) + ". "))
        os.write(History.file_history, str.encode(History.hist + " "))
        History.turn_player = 2
    else:
        History.player2_move = move_player
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

def get_move_player(table, tmp_table, path_pieces, entity, check):
    piece = str(get_piece(tmp_table, path_pieces, entity))
    status = str(get_status(tmp_table, path_pieces, entity))
    if piece != "":
        move_player = piece + str(path_pieces[0][0]) + status + str(path_pieces[1][0])
    else:
        move_player = str(path_pieces[0][0]) + status + str(path_pieces[1][0])

    evolve = str(get_evolve(table, tmp_table, path_pieces, entity))
    if evolve != "":
        move_player = move_player + evolve

    if check == 2:
        move_player = move_player + "+"

    castling = get_castling(tmp_table, path_pieces, entity)
    if castling == 1:
        move_player = "O-O-O"
    elif castling == 2:
        move_player = "O-O"
    return (move_player)

def get_piece(tmp_table, path_pieces, entity):
    piece = ""
    for i in range(2):
        if tmp_table[path_pieces[0][1]][path_pieces[0][2]] == entity[i][1]:
            piece = "N"
        if tmp_table[path_pieces[0][1]][path_pieces[0][2]] == entity[i][2]:
            piece = "B"
        if tmp_table[path_pieces[0][1]][path_pieces[0][2]] == entity[i][3]:
            piece = "R"
        if tmp_table[path_pieces[0][1]][path_pieces[0][2]] == entity[i][4]:
            piece = "Q"
        if tmp_table[path_pieces[0][1]][path_pieces[0][2]] == entity[i][5]:
            piece = "K"
    return (piece)

def get_status(tmp_table, path_pieces, entity):
    if tmp_table[path_pieces[0][1]][path_pieces[0][2]] in entity[0]:
        if tmp_table[path_pieces[1][1]][path_pieces[1][2]] in entity[1]:
            status = "x"
        else:
            status = "-"
    elif tmp_table[path_pieces[0][1]][path_pieces[0][2]] in entity[1]:
        if tmp_table[path_pieces[1][1]][path_pieces[1][2]] in entity[0]:
            status = "x"
        else:
            status = "-"
    return (status)

def get_evolve(table, tmp_table, path_pieces, entity):
    evolve = ""
    for i in range(2):
        if tmp_table[path_pieces[0][1]][path_pieces[0][2]] == entity[i][0]:
            if table[path_pieces[1][1]][path_pieces[1][2]] == entity[i][1]:
                evolve = "=N"
            if table[path_pieces[1][1]][path_pieces[1][2]] == entity[i][2]:
                evolve = "=B"
            if table[path_pieces[1][1]][path_pieces[1][2]] == entity[i][3]:
                evolve = "=R"
            if table[path_pieces[1][1]][path_pieces[1][2]] == entity[i][4]:
                evolve = "=Q"
    return (evolve)

def get_castling(tmp_table, path_pieces, entity):
    castling = ""
    for i in range (2):
        if tmp_table[path_pieces[0][1]][path_pieces[0][2]] == entity[i][5]:
            if tmp_table[path_pieces[1][1]][path_pieces[1][2]] == entity[i][3]:
                if path_pieces[1][2] == 1:
                    castling = 1
                elif path_pieces[1][2] == 8:
                    castling = 2
    return (castling)