import os
import numpy as np
import pandas as pd


class Battleship:

    # TODO: ADD DIFFICULTY BY INCREASING/DECREASING BOARD SIZE
    # TODO: ADD METHODS TO SET BOARD SIZE
    # TODO: CONVERT TO MVC

    def __init__(self):
        self.__COL_HEADER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

        self.__ROW_HEADER = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.__SIZE = self.__NUM_ROWS, self.__NUM_COLS = (10, 10)

        self.__board = self.__create_game_board()

    def __create_game_board(self) -> pd.DataFrame:
        """
        Creates the game board

        :returns Returns a game board of type pd.DataFrame
        """

        board = np.zeros(self.__SIZE, dtype=str)

        # TODO: list comprehension
        for i in range(self.__NUM_ROWS):
            for j in range(self.__NUM_COLS):
                board[i, j] = '-'

        return pd.DataFrame(board, index=self.__ROW_HEADER, columns=self.__COL_HEADER)

    @staticmethod
    def welcome_message() -> None:
        """ Prints welcome message """

        print("\n\n         WELCOME TO BATTLESHIP")
        print("=========================================\n\n")

    @staticmethod
    def main_menu_msg() -> None:
        """ Prints Main Menu """

        print("1) Start New Game")
        print("2) Load Game")
        print("3) Quit")

    @staticmethod
    def clear_screen_win() -> None:
        """ Clears screen on Windows machines """
        os.system('cls')

    @staticmethod
    def clear_screen_nix() -> None:
        """ Clears screen on *Nix machines """
        os.system('clear')

