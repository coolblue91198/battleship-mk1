import numpy as np
import pandas as pd
import os
import time
import random


class BattleShip:

    def __init__(self):
        # Number of ships
        self.own_ships = 4
        self.enemy_ships = 4
        self.placed_ships = 0
        self.placed_enemy_ships = 0

        # Board Size
        self.m = 11
        self.n = 11

        # Board Headers
        self.cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']  # Define Column Heading
        self.headers = dict(enumerate(self.cols))  # Headers
        self.rows = list(self.headers.keys())  # Define Row Heading

        # Make Board
        self.board = self.create_board()

        # Locations of placed ships
        self.used_pos = []

        # Define Ships
        self.battleship = {
            "id": 1,
            "name": "Battleship",
            "size": 4,
            "placed": False
        }
        self.cruiser = {
            "id": 2,
            "name": "Cruiser",
            "size": 3,
            "placed": False
        }
        self.destroyer = {
            "id": 3,
            "name": "Destroyer",
            "size": 2,
            "placed": False
        }
        self.sumbarine = {
            "id": 4,
            "name": "Submarine",
            "size": 1,
            "placed": False
        }

    def create_board(self) -> pd.DataFrame:
        """ Creates the game board and returns to __init__"""

        board_array = np.zeros((self.m, self.n), dtype=str)  # Define Array to iterate through

        # Replace zeros with '-'
        for i in range(self.m):
            for j in range(self.n):
                board_array[i, j] = '-'

        # Create Pandas Dataframe to represent the board
        board = pd.DataFrame(data=board_array, index=self.rows, columns=self.cols)

        return board

    @staticmethod
    def welcome_msg():
        print('                               ')
        print('                      WELCOME TO BATTLESHIP')
        print('==============================================================================')
