#!/usr/bin/python3

import os
from datetime import datetime as dt

class History:
    hist_display = ""
    hist_technique = []
    turn_player = 1
    turn_game = 1
    player1_move = ""
    player2_move = ""
    file_history = ""
    @classmethod
    def history(cls, table, tmp_table, path_pieces, entity, check):
        move_player = GetInformation.get_move_player(table, tmp_table, path_pieces, entity, check)
        if cls.turn_player == 1:
            cls.player1_move = move_player
            cls.hist_display = cls.player1_move
            os.write(cls.file_history, str.encode(str(cls.turn_game) + ". "))
            os.write(cls.file_history, str.encode(cls.hist_display + " "))
            cls.turn_player = 2
        else:
            cls.player2_move = move_player
            cls.hist_display = cls.player2_move
            os.write(cls.file_history, str.encode(cls.hist_display))
            os.write(cls.file_history, str.encode("\n"))
            cls.hist_technique.append([cls.player1_move, cls.player2_move])
            print(cls.hist_technique)
            cls.turn_player = 1
            cls.turn_game += 1
        return
    

class Os:
    path_dirs = ""
    name_file = ""
    path_file = ""
    def __init__(self, user):
        self.name_file = str(dt.now().date()) + "_" + str(dt.now().timetuple().tm_hour) + ":" + str(dt.now().timetuple().tm_min) + "." + str(dt.now().timetuple().tm_sec) + "_" + str(user[0]) + "_versus_" + str(user[1]) + ".pgn"
        self.path_dirs = "./game/"
        self.path_file = self.path_dirs + self.name_file
    def os_operation(self, user):
        if not os.path.exists(self.path_dirs):
            os.makedirs(self.path_dirs)
        if not os.path.exists(self.path_file):
            History.file_history = os.open(self.path_file, os.O_CREAT|os.O_RDWR)
            os.write(History.file_history, str.encode('[Event "'+str(user[0])+' / '+str(user[1])+'"]\n[Date "'+str(dt.now().date())+'"]\n[White "'+str(user[0])+'"]\n[Black "'+str(user[1])+'"]\n'))
        return

class GetInformation:
    @classmethod
    def get_move_player(cls,table, tmp_table, path_pieces, entity, check):
        piece = str(GetInformation.get_piece(tmp_table, path_pieces, entity))
        status = str(GetInformation.get_status(tmp_table, path_pieces, entity))
        if piece != "":
            move_player = piece + str(path_pieces[0][0]) + status + str(path_pieces[1][0])
        else:
            move_player = str(path_pieces[0][0]) + status + str(path_pieces[1][0])
        evolve = str(GetInformation.get_evolve(table, tmp_table, path_pieces, entity))
        if evolve != "":
            move_player = move_player + evolve
        if check == 2:
            move_player = move_player + "+"
        castling = GetInformation.get_castling(tmp_table, path_pieces, entity)
        if castling == 1:
            move_player = "O-O-O"
        elif castling == 2:
            move_player = "O-O"
        return (move_player)

    @classmethod
    def get_piece(cls, tmp_table, path_pieces, entity):
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

    @classmethod
    def get_status(cls, tmp_table, path_pieces, entity):
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

    @classmethod
    def get_evolve(cls, table, tmp_table, path_pieces, entity):
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

    @classmethod
    def get_castling(cls, tmp_table, path_pieces, entity):
        castling = ""
        for i in range (2):
            if tmp_table[path_pieces[0][1]][path_pieces[0][2]] == entity[i][5]:
                if tmp_table[path_pieces[1][1]][path_pieces[1][2]] == entity[i][3]:
                    if path_pieces[1][2] == 1:
                        castling = 1
                    elif path_pieces[1][2] == 8:
                        castling = 2
        return (castling)