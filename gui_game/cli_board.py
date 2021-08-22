def create_board(turn, np_x, apb_y, np_omok_board):
    import numpy as np
    cli_black = 1
    cli_white = 2

    if turn % 2 == 1:
        turn_type = "black"
    else:
        turn_type = "white"

    if apb_y == "a":
        np_y = 0
    if apb_y == "b":
        np_y = 1
    if apb_y == "c":
        np_y = 2
    if apb_y == "d":
        np_y = 3
    if apb_y == "e":
        np_y = 4
    if apb_y == "f":
        np_y = 5
    if apb_y == "g":
        np_y = 6
    if apb_y == "h":
        np_y = 7
    if apb_y == "i":
        np_y = 8
    if apb_y == "j":
        np_y = 9
    if apb_y == "k":
        np_y = 10
    if apb_y == "l":
        np_y = 11
    if apb_y == "n":
        np_y = 12
    if apb_y == "m":
        np_y = 13
    if apb_y == "o":
        np_y = 14
    
    if np_omok_board[np_y, np_x] != 0:
        return np_omok_board, turn, True, np_x, np_y
    else:
        if turn_type == "black":
            np_omok_board[np_y, np_x] = 1
        elif turn_type == "white":
            np_omok_board[np_y, np_x] = 2
        return np_omok_board, turn, False, np_x, np_y







"""
import numpy as np
import os

def play(turn):
    while run:

        if turn % 2 == 1:
            turn_type = "black"
        else:
            turn_type = "white"
        
        row_point, column_point = map(int, input("row, column : ").split(","))
        
        if omok_board[row_point - 1, column_point - 1] != 0:

        else:
            if turn_type == "black":
                omok_board[row_point - 1, column_point - 1] = black
            elif turn_type == "white":
                omok_board[row_point - 1, column_point - 1] = white
            turn += 1

size = 15
omok_board = np.zeros([size, size])
black = 1
white = 2
first_turn = 1
run = True

play(first_turn)
"""