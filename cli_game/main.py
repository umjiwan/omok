import numpy as np
import os

def play(turn):
    while run:
        if run == 12:
            print(303030)
        else:
            os.system("clear")
            
            print(omok_board)

            if turn % 2 == 1:
                turn_type = "black"
            else:
                turn_type = "white"
        
            print("")
            print(turn_type)
            
            row_point, column_point = map(int, input("row, column : ").split(","))

            print(f"{row_point}, {column_point}")
        
            print("")
            
            if omok_board[row_point - 1, column_point - 1] != 0:
                print("nope")
            else:
                if turn_type == "black":
                    omok_board[row_point - 1, column_point - 1] = black
                elif turn_type == "white":
                    omok_board[row_point - 1, column_point - 1] = white
                turn += 1

size = 15
omok_board = np.zeros([size, size])
omok_overlap = 0
black = 1
white = 2

first_turn = 1
run = True

play(first_turn)