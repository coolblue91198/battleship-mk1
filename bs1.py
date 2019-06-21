import numpy as np
import pandas as pd
import os
import time
import random


class BattleShip:
    """Class for all battleship game objects"""

    def __init__(self):
        # Number of ships
        self.own_ships = 4
        self.enemy_ships = 4
        self.placed_ships = 0
        self.placed_enemy_ships = 0

        # Board Size
        self.m = 11
        self.n = 11

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

        # Define Board
        self.cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']  # Define Column Heading

        self.headers = dict(enumerate(self.cols))  # Headers

        self.rows = list(self.headers.keys())  # Define Row Heading

        board_array = np.zeros((self.m, self.n), dtype=str)  # Define Array to iterate through

        # Replace zeros with '-'
        for i in range(self.m):
            for j in range(self.n):
                board_array[i, j] = '-'

        # Create Pandas Dataframe to represent the board
        self.board = pd.DataFrame(data=board_array, index=self.rows, columns=self.cols)

        # Print Introduction and Show Boards
        print('                               ')
        print('                      WELCOME TO BATTLESHIP')
        print('==============================================================================')
        self.print_player_board()

    # self.print_enemy_board()

    def find_index(self, col_loc):
        '''Finds index for column name'''
        for i in range(len(self.headers)):
            if self.headers[i] == col_loc:
                return i

    def print_player_board(self):
        print("Player Board")
        print('******************************************************************************')
        print(self.board)
        print('******************************************************************************')

    def print_enemy_board(self):
        print("Opponent Board")
        print('******************************************************************************')
        print(self.board)
        print('==============================================================================')

    def clear_screen(self):
        os.system('clear')

    def loc_used(self, row_loc, col_loc):
        '''Checks if the given position has been used already'''
        if (col_loc + str(row_loc)) in self.used_pos:
            return True
        else:
            return False

    def get_row(self):
        row_loc = input('Enter Row number [0-10]: ')
        while row_loc not in str(self.rows):
            row_loc = input('Enter Row number [0-10]: ')
        return int(row_loc)

    def valid_row(self, row_loc):
        while row_loc not in self.board.index:
            print("kk")
            self.get_row()

    def get_col(self):
        col_loc = input('Enter Column [A-K]: ').upper()
        return col_loc

    def valid_col(self, col_loc):
        while col_loc not in self.board.columns:
            self.get_col()

    def place_battleship(self, row_loc=None, col_loc=None):
        if self.battleship['placed'] == False:
            location = input('Place Horizontal or Vertical? [h/v]: ')
            while location.lower() != 'h' and location.lower() != 'v':
                location = input('Place Horizontal or Vertical? [h/v]: ')
            # Horizontal Placement
            if location.lower() == 'h':
                # Get row from user
                if row_loc == None:
                    row_loc = self.get_row()

                # Check that user input is a valid row
                self.valid_row(row_loc)

                # Get column from user
                if col_loc == None:
                    col_loc = self.get_col()

                # Check that user input is a valid column
                self.valid_col(col_loc)

                # Make sure no other ships are there
                while self.loc_used(row_loc, col_loc) == True:
                    print("Another ship is in this location!")
                    row_loc = self.get_row()
                    self.valid_row(row_loc)
                    col_loc = self.get_col()
                    self.valid_col(col_loc)

                # Check that ship can fit in given space
                while (self.n - self.find_index(col_loc)) < self.battleship['size']:
                    col_loc = input('Battleship cannot fit, please enter another column: ').upper()

                # Place ship
                for i in range(self.battleship['size'] - 1):
                    while self.loc_used(row_loc, self.board.columns.values[i + 1 + self.find_index(col_loc)]) == True:
                        print("Another ship is in this location!")
                        row_loc = self.get_row()
                        self.valid_row(row_loc)
                        col_loc = self.get_col()
                        self.valid_col(col_loc)
                    else:
                        self.board.iloc[row_loc].loc[col_loc:self.board.columns[i + 1 + self.find_index(col_loc)]] = 'x'

                self.used_pos.append(col_loc + str(row_loc))

            # Vertical Placement
            if location.lower() == 'v':
                # Get column
                if col_loc == None:
                    col_loc = self.get_col()

                # Check that user input is a valid column
                self.valid_col(col_loc)

                # Get row
                if row_loc == None:
                    row_loc = self.get_row()

                # Check that user input is a valid row
                self.valid_row(row_loc)

                # Make sure no other ships are there
                while self.loc_used(row_loc, col_loc) == True:
                    print("Another ship is in this location!")
                    row_loc = self.get_row()
                    self.valid_row(row_loc)
                    col_loc = self.get_col()
                    self.valid_col(col_loc)

                # Check that ship can fit in given space
                while (self.m - row_loc) < self.battleship['size']:
                    row_loc = int(input('Battleship cannot fit, please enter another row: '))

                # Place Ship
                for i in range(self.battleship['size'] - 1):
                    while self.loc_used(i + 1 + row_loc, col_loc) == True:
                        print("Another ship is in this location!")
                        row_loc = self.get_row()
                        self.valid_row(row_loc)
                        col_loc = self.get_col()
                        self.valid_col(col_loc)
                    else:
                        self.board.loc[row_loc:i + 1 + row_loc, col_loc] = 'x'
                        self.used_pos.append(col_loc + str(i + 1 + row_loc))

                self.used_pos.append(col_loc + str(row_loc))

            # Display updated board, update required variables
            self.battleship["placed"] = True
            self.placed_ships += 1
            self.clear_screen()
            self.print_player_board()
            print('%d ships remaining!' % (self.own_ships - self.placed_ships))

        else:
            print("This ship has already been placed!")
            time.sleep(1)
            self.clear_screen()
            self.print_player_board()

    def place_cruiser(self, row_loc=None, col_loc=None):
        if self.cruiser['placed'] == False:
            location = input('Place Horizontal or Vertical? [h/v]: ')
            while location.lower() != 'h' and location.lower() != 'v':
                location = input('Place Horizontal or Vertical? [h/v]: ')
            # Horizontal Placement
            if location.lower() == 'h':
                # Get row from user
                if row_loc == None:
                    row_loc = self.get_row()

                # Check that user input is a valid row
                self.valid_row(row_loc)

                # Get column from user
                if col_loc == None:
                    col_loc = self.get_col()

                # Check that user input is a valid column
                self.valid_col(col_loc)

                # Make sure no other ships are there
                while self.loc_used(row_loc, col_loc) == True:
                    print("Another ship is in this location!")
                    row_loc = self.get_row()
                    self.valid_row(row_loc)
                    col_loc = self.get_col()
                    self.valid_col(col_loc)

                # Check that ship can fit in given space
                while (self.n - self.find_index(col_loc)) < self.cruiser['size']:
                    col_loc = input('Cruiser cannot fit, please enter another column: ').upper()

                # Place ship
                for i in range(self.cruiser['size'] - 1):
                    while self.loc_used(row_loc, self.board.columns.values[i + 1 + self.find_index(col_loc)]) == True:
                        print("Another ship is in this location!")
                        row_loc = self.get_row()
                        self.valid_row(row_loc)
                        col_loc = self.get_col()
                        self.valid_col(col_loc)
                    else:
                        self.board.iloc[row_loc].loc[col_loc:self.board.columns[i + 1 + self.find_index(col_loc)]] = 'x'

                self.used_pos.append(col_loc + str(row_loc))

            # Vertical Placement
            if location.lower() == 'v':
                # Get column
                if col_loc == None:
                    col_loc = self.get_col()

                # Check that user input is a valid column
                self.valid_col(col_loc)

                # Get row
                if row_loc == None:
                    row_loc = self.get_row()

                # Check that user input is a valid row
                self.valid_row(row_loc)

                # Make sure no other ships are there
                while self.loc_used(row_loc, col_loc) == True:
                    print("Another ship is in this location!")
                    row_loc = self.get_row()
                    self.valid_row(row_loc)
                    col_loc = self.get_col()
                    self.valid_col(col_loc)

                # Check that ship can fit in given space
                while (self.m - row_loc) < self.cruiser['size']:
                    row_loc = int(input('Cruiser cannot fit, please enter another row: '))

                # Place Ship
                for i in range(self.cruiser['size'] - 1):
                    while self.loc_used(i + 1 + row_loc, col_loc) == True:
                        print("Another ship is in this location!")
                        row_loc = self.get_row()
                        self.valid_row(row_loc)
                        col_loc = self.get_col()
                        self.valid_col(col_loc)
                    else:
                        self.board.loc[row_loc:i + 1 + row_loc, col_loc] = 'x'
                        self.used_pos.append(col_loc + str(i + 1 + row_loc))

                self.used_pos.append(col_loc + str(row_loc))

            # Display updated board, update required variables
            self.cruiser["placed"] = True
            self.placed_ships += 1
            self.clear_screen()
            self.print_player_board()
            print('%d ships remaining!' % (self.own_ships - self.placed_ships))

        else:
            print("This ship has already been placed!")
            time.sleep(1)
            self.clear_screen()
            self.print_player_board()

    def place_destroyer(self, row_loc=None, col_loc=None):
        if self.destroyer['placed'] == False:
            location = input('Place Horizontal or Vertical? [h/v]: ')
            while location.lower() != 'h' and location.lower() != 'v':
                location = input('Place Horizontal or Vertical? [h/v]: ')
            # Horizontal Placement
            if location.lower() == 'h':
                # Get row from user
                if row_loc == None:
                    row_loc = self.get_row()

                # Check that user input is a valid row
                self.valid_row(row_loc)

                # Get column from user
                if col_loc == None:
                    col_loc = self.get_col()

                # Check that user input is a valid column
                self.valid_col(col_loc)

                # Make sure no other ships are there
                while self.loc_used(row_loc, col_loc) == True:
                    print("Another ship is in this location!")
                    row_loc = self.get_row()
                    self.valid_row(row_loc)
                    col_loc = self.get_col()
                    self.valid_col(col_loc)

                # Check that ship can fit in given space
                while (self.n - self.find_index(col_loc)) < self.destroyer['size']:
                    col_loc = input('Destroyer cannot fit, please enter another column: ').upper()

                # Place ship
                for i in range(self.destroyer['size'] - 1):
                    while self.loc_used(row_loc, self.board.columns.values[i + 1 + self.find_index(col_loc)]) == True:
                        print("Another ship is in this location!")
                        row_loc = self.get_row()
                        self.valid_row(row_loc)
                        col_loc = self.get_col()
                        self.valid_col(col_loc)
                    else:
                        self.board.iloc[row_loc].loc[col_loc:self.board.columns[i + 1 + self.find_index(col_loc)]] = 'x'

                self.used_pos.append(col_loc + str(row_loc))

            # Vertical Placement
            if location.lower() == 'v':
                # Get column
                if col_loc == None:
                    col_loc = self.get_col()

                # Check that user input is a valid column
                self.valid_col(col_loc)

                # Get row
                if row_loc == None:
                    row_loc = self.get_row()

                # Check that user input is a valid row
                self.valid_row(row_loc)

                # Make sure no other ships are there
                while self.loc_used(row_loc, col_loc) == True:
                    print("Another ship is in this location!")
                    row_loc = self.get_row()
                    self.valid_row(row_loc)
                    col_loc = self.get_col()
                    self.valid_col(col_loc)

                # Check that ship can fit in given space
                while (self.m - row_loc) < self.destroyer['size']:
                    row_loc = int(input('Destroyer cannot fit, please enter another row: '))

                # Place Ship
                for i in range(self.destroyer['size'] - 1):
                    while self.loc_used(i + 1 + row_loc, col_loc) == True:
                        print("Another ship is in this location!")
                        row_loc = self.get_row()
                        self.valid_row(row_loc)
                        col_loc = self.get_col()
                        self.valid_col(col_loc)
                    else:
                        self.board.loc[row_loc:i + 1 + row_loc, col_loc] = 'x'
                        self.used_pos.append(col_loc + str(i + 1 + row_loc))

                self.used_pos.append(col_loc + str(row_loc))

            # Display updated board, update required variables
            self.destroyer["placed"] = True
            self.placed_ships += 1
            self.clear_screen()
            self.print_player_board()
            print('%d ships remaining!' % (self.own_ships - self.placed_ships))

        else:
            print("This ship has already been placed!")
            time.sleep(1)
            self.clear_screen()
            self.print_player_board()

    def place_submarine(self, row_loc=None, col_loc=None):
        if self.sumbarine['placed'] == False:
            # Get row
            if row_loc == None:
                row_loc = self.get_row()
            # Validate row
            self.valid_row(row_loc)
            # Get col
            if col_loc == None:
                col_loc = self.get_col()
            # Validate col
            self.valid_col(col_loc)

            # Make sure no other ships are there
            while self.loc_used(row_loc, col_loc) == True:
                print("Another ship is in this location!")
                row_loc = self.get_row()
                self.valid_row(row_loc)
                col_loc = self.get_col()
                self.valid_col(col_loc)

            # Place Ship
            self.board.loc[row_loc, col_loc] = 'x'

            # Display updated board, update required variables
            self.sumbarine["placed"] = True
            self.placed_ships += 1
            self.clear_screen()
            self.print_player_board()
            print('%d ships remaining!' % (self.own_ships - self.placed_ships))

        else:
            print("This ship has already been placed!")
            time.sleep(1)
            self.clear_screen()
            self.print_player_board()

    def place_ships(self):
        """Places ships in specified postion"""

        # Prompt user for ship choice to place
        while self.placed_ships < 4:
            print("")
            print("Which ship would you like to place?")
            print("#   NAME        SIZE")
            print("1) Battleship 	[4]")
            print("2) Cruiser 	[3]")
            print("3) Destroyer 	[2]")
            print("4) Submarine 	[1]")
            choice = input('Please enter [1-4]: ')
            print("")

            # Place specified ship
            if choice == '1':  # Battleship
                self.place_battleship()
            elif choice == '2':  # Cruiser
                self.place_cruiser()
            elif choice == '3':  # Destroyer
                self.place_destroyer()
            elif choice == '4':  # Submarine
                self.place_submarine()

    def ai_board(self):
        pass

    def test(self):
        valid_rows = self.rows
        valid_cols = self.cols
        rand_row = random.choice(valid_rows)
        rand_col = random.choice(valid_cols)
        valid_rows.remove(rand_row)
        valid_cols.remove(rand_col)
    # Finish This Up!!
    # Save Board after each ship is placed!!


if __name__ == '__main__':
    bs = BattleShip()
    bs.place_ships()
# bs.ai_board(battleship)
# bs.test()
