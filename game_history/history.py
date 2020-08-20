#!/usr/bin/python3


class History:
    hist = []
    turn = 1
    player1_move = ""
    player2_move = ""

def history(table, tmp_table, path_pieces, entity):
    if History.turn == 1:
        History.player1_move = str(path_pieces[0][0])+"-"+str(path_pieces[1][0])
        History.turn = 2
    else:
        History.player2_move = str(path_pieces[0][0])+"-"+str(path_pieces[1][0])
        History.hist.append([History.player1_move, History.player2_move])
        History.turn = 1
    return