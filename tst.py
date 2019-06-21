import os
import numpy as np
import pandas as pd


def welcome_message() -> None:
    """ Prints welcome message """

    print("\n\n         WELCOME TO BATTLESHIP")
    print("=========================================\n\n")


def main_menu_msg() -> None:
    """ Prints Main Menu """

    print("1) Start New Game")
    print("2) Load Game")
    print("3) Quit")


def clear_screen_win() -> None:
    """ Clears screen on Windows machines """
    os.system('cls')


def clear_screen_nix() -> None:
    """ Clears scrren on *Nix machines """
    os.system('clear')


def create_game_board() -> pd.DataFrame:
    """ Creates the game board """

    COL_HEADER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    ROW_HEADER = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    SIZE = NUM_ROWS, NUM_COLS = (10, 10)

    board = np.zeros(SIZE, dtype=str)

    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            board[i, j] = '-'

    board = pd.DataFrame(board, index=ROW_HEADER, columns=COL_HEADER)

    return board


def print_board(board: pd.DataFrame) -> None:
    print(board)


def main_menu_choice():
    """ Gets user input for main menu """

    main_choice = str(input("Please enter menu choice (1-3): "))

    if main_choice is "1":
        pass
    elif main_choice is "2":
        pass
    elif main_choice is "3":
        pass
    else:
        print("Please enter valid menu choice (1-3): ")


clear_screen_win()
welcome_message()
main_menu_msg()






