#!/usr/bin/python3

king_pose_before = ["",""]
king_pose_after = ["",""]



def check(table, tmp_table, user, entity):
    if user[2] == 1:
        if user[3] != 1:
            for i in range (1,9):
                for j in range (1,9):
                    if tmp_table[i][j] == entity[1][5]:
                        king_pose_before[0] = i
                        king_pose_before[1] = j
                    if table[i][j] == entity[1][5]:
                        king_pose_after[0] = i
                        king_pose_after[1] = j
            if check_verification(tmp_table, entity[0], entity[1], entity[2], king_pose_before, user) == True:
                if check_verification(table, entity[0], entity[1], entity[2],king_pose_after, user) == True:
                    return (1)
                else:
                    return (0)
            else:
                if check_verification(table, entity[0], entity[1], entity[2],king_pose_after, user) == True:
                    return (2)
                else:
                    return (0)
        elif user[3] == 1:
            for i in range (1,9):
                for j in range (1,9):
                    if tmp_table[i][j] == entity[0][5]:
                        king_pose_before[0] = i
                        king_pose_before[1] = j
                    if table[i][j] == entity[0][5]:
                        king_pose_after[0] = i
                        king_pose_after[1] = j
            if check_verification(tmp_table, entity[1], entity[0], entity[2], king_pose_before, user) == True:
                if check_verification(table, entity[1], entity[0], entity[2],king_pose_after, user) == True:
                    return (2)
                else:
                    return (0)
    elif user[2] == 2:
        if user[3] != 1:
            for i in range (1,9):
                for j in range (1,9):
                    if tmp_table[i][j] == entity[0][5]:
                        king_pose_before[0] = i
                        king_pose_before[1] = j
                    if table[i][j] == entity[0][5]:
                        king_pose_after[0] = i
                        king_pose_after[1] = j
            if check_verification(tmp_table, entity[1], entity[0], entity[2], king_pose_before, user) == True:
                if check_verification(table, entity[1], entity[0], entity[2],king_pose_after, user) == True:
                    return (1)
                else:
                    return (0)
            else:
                if check_verification(table, entity[1], entity[0], entity[2],king_pose_after, user) == True:
                    return (2)
                else:
                    return (0)
        elif user[3] == 1:
            for i in range (1,9):
                for j in range (1,9):
                    if tmp_table[i][j] == entity[1][5]:
                        king_pose_before[0] = i
                        king_pose_before[1] = j
                    if table[i][j] == entity[1][5]:
                        king_pose_after[0] = i
                        king_pose_after[1] = j
            if check_verification(tmp_table, entity[0], entity[1], entity[2], king_pose_before, user) == True:
                if check_verification(table, entity[0], entity[1], entity[2],king_pose_after, user) == True:
                    return (2)
                else:
                    return (0)

def check_verification(board, entity_ad, entity_me, empty_space, king_pose, user):
    try:
        for i in range (1,9):
            if (king_pose[0]+i > 8):
                break
            if board[king_pose[0]+i][king_pose[1]] != empty_space[0]:        #⭣
                if board[king_pose[0]+i][king_pose[1]] in entity_me:
                    break
                elif board[king_pose[0]+i][king_pose[1]] == entity_ad[3] or board[king_pose[0]+i][king_pose[1]] == entity_ad[4]:
                    return (True)
    except IndexError:
        pass
    
    try:
        for i in range (1,9):
            if (king_pose[0]-i < 1):
                break
            if board[king_pose[0]-i][king_pose[1]] != empty_space[0]:        #⭡
                if board[king_pose[0]-i][king_pose[1]] in entity_me:
                    break
                elif board[king_pose[0]-i][king_pose[1]] == entity_ad[3] or board[king_pose[0]-i][king_pose[1]] == entity_ad[4]:
                    return (True)
    except IndexError:
        pass

    try:
        for i in range (1,9):
            if (king_pose[1]+i > 8):
                break
            if board[king_pose[0]][king_pose[1]+i] != empty_space[0]:        #⭢
                if board[king_pose[0]][king_pose[1]+i] in entity_me:
                    break
                elif board[king_pose[0]][king_pose[1]+i] == entity_ad[3] or board[king_pose[0]][king_pose[1]+i] == entity_ad[4]:
                    return (True)
    except IndexError:
        pass

    try:
        for i in range (1,9):
            if (king_pose[1]-i < 0):
                break
            if board[king_pose[0]][king_pose[1]-i] != empty_space[0]:        #⭠
                if board[king_pose[0]][king_pose[1]-i] in entity_me:
                    break
                elif board[king_pose[0]][king_pose[1]-i] == entity_ad[3] or board[king_pose[0]][king_pose[1]-i] == entity_ad[4]:
                    return (True)
    except IndexError:
        pass

    try:
        for i in range (1,9):
            if (king_pose[0]+i > 8 or king_pose[1]+i > 8):
                break
            if board[king_pose[0]+i][king_pose[1]+i] != empty_space[0]:      #⭨
                if board[king_pose[0]+i][king_pose[1]+i] in entity_me:
                    break
                elif user[2] == 2 and board[king_pose[0]+1][king_pose[1]+1] == entity_ad[0]:
                    return (True)
                elif board[king_pose[0]+i][king_pose[1]+i] == entity_ad[2] or board[king_pose[0]+i][king_pose[1]+i] == entity_ad[4]:
                    return (True)
    except IndexError:
        pass

    try:
        for i in range (1,9):
            if (king_pose[0]+i > 8 or king_pose[1]-i < 0):
                break
            if board[king_pose[0]+i][king_pose[1]-i] != empty_space[0]:      #⭩
                if board[king_pose[0]+i][king_pose[1]-i] in entity_me:
                    break
                elif user[2] == 2 and board[king_pose[0]+1][king_pose[1]-1] == entity_ad[0]:
                    return (True)
                elif board[king_pose[0]+i][king_pose[1]-i] == entity_ad[2] or board[king_pose[0]+i][king_pose[1]-i] == entity_ad[4]:
                    return (True)
    except IndexError:
        pass

    try:
        for i in range (1,9):
            if (king_pose[0]-i < 0 or king_pose[1]+i > 8):
                break
            if board[king_pose[0]-i][king_pose[1]+i] != empty_space[0]:      #⭧
                if board[king_pose[0]-i][king_pose[1]+i] in entity_me:
                    break
                elif user[2] == 1 and board[king_pose[0]-1][king_pose[1]+1] == entity_ad[0]:
                    return (True)
                elif board[king_pose[0]-i][king_pose[1]+i] == entity_ad[2] or board[king_pose[0]-i][king_pose[1]+i] == entity_ad[4]:
                    return (True)
    except IndexError:
        pass

    try:
        for i in range (1,9):
            if (king_pose[0]-i < 0 or king_pose[1]-i < 0):
                break
            if board[king_pose[0]-i][king_pose[1]-i] != empty_space[0]:      #⭦
                if board[king_pose[0]-i][king_pose[1]-i] in entity_me:
                    break
                elif user[2] == 1 and board[king_pose[0]-1][king_pose[1]-1] == entity_ad[0]:
                    return (True)
                elif board[king_pose[0]-i][king_pose[1]-i] == entity_ad[2] or board[king_pose[0]-i][king_pose[1]-i] == entity_ad[4]:
                    return (True)
    except IndexError:
        pass

    try:
        if (king_pose[0]+2 > 8 or king_pose[1]+1 > 8):
            pass
        elif board[king_pose[0]+2][king_pose[1]+1] == entity_ad[1]:     #⮧
            return (True)
    except IndexError:
        pass

    try:
        if (king_pose[0]+1 > 8 or king_pose[1]+2 > 8):
            pass
        elif board[king_pose[0]+1][king_pose[1]+2] == entity_ad[1]:     #⮡
            return (True)
    except IndexError:
        pass

    try:
        if (king_pose[0]+2 > 8 or king_pose[1]-1 < 0):
            pass
        elif board[king_pose[0]+2][king_pose[1]-1] == entity_ad[1]:     #⮦
            return (True)
    except IndexError:
        pass

    try:
        if (king_pose[0]+1 > 8 or king_pose[1]-2 < 0):
            pass
        elif board[king_pose[0]+1][king_pose[1]-2] == entity_ad[1]:     #⮠
            return (True)
    except IndexError:
        pass

    try:
        if (king_pose[0]-2 < 0 or king_pose[1]+1 > 8):
            pass
        elif board[king_pose[0]-2][king_pose[1]+1] == entity_ad[1]:     #⮥
            return (True)
    except IndexError:
        pass

    try:
        if (king_pose[0]-1 < 0 or king_pose[1]+2 > 8):
            pass
        elif board[king_pose[0]-1][king_pose[1]+2] == entity_ad[1]:     #⮣
            return (True)
    except IndexError:
        pass

    try:
        if (king_pose[0]-2 < 0 or king_pose[1]-1 < 0):
            pass
        elif board[king_pose[0]-2][king_pose[1]-1] == entity_ad[1]:     #⮤
            return (True)
    except IndexError:
        pass

    try:
        if (king_pose[0]-1 < 0 or king_pose[1]-2 < 0):
            pass
        elif board[king_pose[0]-1][king_pose[1]-2] == entity_ad[1]:     #⮢
            return (True)
    except IndexError:
        pass

    return (False)