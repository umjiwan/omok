def VerticalLine(turn_type, np_x, np_y, omok_board):
    if turn_type == "black":
        turn_num = 1
    elif turn_type == "white":
        turn_num = 2
    score = 1
    
    for i in range(5):
        # 만약 i 가 1이고 
        if omok_board[(np_y) - (i), np_x] == turn_num: # 만약 놓은 값에 y - i 값이 놓은 숫자와 같다면 
            score += 1
        else:
            break

    for i in range(5):
        if omok_board[(np_y) + (i), np_x] == turn_num: # 만약 놓은 값에 y - i 값이 놓은 숫자와 같다면 
            score += 1
        else:
            break

    if score >= 7:
        win = True
    else:
        win = False

    return win

def PlusMinusDiagonal(turn_type, np_x, np_y, omok_board):
    if turn_type == "black":
        turn_num = 1
    elif turn_type == "white":
        turn_num = 2
    score = 1
    
    for i in range(5):
        # 만약 i 가 1이고 
        if omok_board[(np_y) - (i), (np_x) + (i)] == turn_num: # 만약 놓은 값에 y - i 값이 놓은 숫자와 같다면 
            score += 1
        else:
            break

    for i in range(5):
        if omok_board[(np_y) + (i), (np_x) - (i)] == turn_num: # 만약 놓은 값에 y - i 값이 놓은 숫자와 같다면 
            score += 1
        else:
            break

    if score >= 7:
        win = True
    else:
        win = False

    return win

def HorizontalLine(turn_type, np_x, np_y, omok_board):
    if turn_type == "black":
        turn_num = 1
    elif turn_type == "white":
        turn_num = 2
    score = 1
    
    for i in range(5):
        # 만약 i 가 1이고 
        if omok_board[np_y, (np_x) + (i)] == turn_num: # 만약 놓은 값에 y - i 값이 놓은 숫자와 같다면 
            score += 1
        else:
            break

    for i in range(5):
        if omok_board[np_y, (np_x) - (i)] == turn_num: # 만약 놓은 값에 y - i 값이 놓은 숫자와 같다면 
            score += 1
        else:
            break

    if score >= 7:
        win = True
    else:
        win = False

    return win

def MinusPlusDiagonal(turn_type, np_x, np_y, omok_board):
    if turn_type == "black":
        turn_num = 1
    elif turn_type == "white":
        turn_num = 2
    score = 1
    
    for i in range(5):
        # 만약 i 가 1이고 
        if omok_board[(np_y) + (i), (np_x) + (i)] == turn_num: # 만약 놓은 값에 y - i 값이 놓은 숫자와 같다면 
            score += 1
        else:
            break

    for i in range(5):
        if omok_board[(np_y) - (i), (np_x) - (i)] == turn_num: # 만약 놓은 값에 y - i 값이 놓은 숫자와 같다면 
            score += 1
        else:
            break

    if score >= 7:
        win = True
    else:
        win = False

    return win
    
    



    
    
