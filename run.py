# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random # python module for generating random integers

def welcome():
    print("\nWelcome to Battleships!\n")
    # while loop runs until player provides a valid input
    while True:
        # provides player input field and converts text to lowercase to match the checks below
        game = input("Would you like to play a game? (y/n): ").lower()
        if game == "n":
            print("Maybe another time. Goodbye!")
            quit()
        if game == "y":
            print("\nLet's play!\n")
            break
        else:
            print("That is not a valid input. Please try again.")
            continue

class GameBoard: 
    def __init__(self,size):
        """
        Initialise the GameBoard class
        """
        # define the GameBoard attributes
        self.size = size # the GameBoard has a size (player defined)
        self.board = [["." for x in range(size)] for y in range(size)] # the GameBoard board is a list of x, y coordinates with a range of sizes
        self.total_cells = size * size # the GameBoard has a total number of cells 
        self.num_ships = (self.total_cells * 20) // 100 # 20% of the GameBoard cells are ships
        self.place_random_ships() # ships are placed randomly on the GameBoard when this method is called

    def place_random_ships(self):
        """
        place ships randomly on the board
        """
        # create a list of all possible coordinates
        all_coordinates = [(x, y) for x in range(self.size) for y in range(self.size)]
        # randomly choose ship positions from the all_coordinates list
        ship_positions = random.sample(all_coordinates, self.num_ships)

        # itertae ship placement using "S" to represent ships
        for x, y in ship_positions:
            self.board[x][y] = "S"

    def print_board(self):
        """
        Print the GameBoard
        """
        # iterate column headers A - ? beginning with a double space for alignment purposes
        # chr(65 + i) - indexing begins with capital 'A' (65th character in ASCII)
        print("  " + " ".join([chr(65 + i) for i in range(self.size)]))
        # use enumerate() to return both row index (i) and row content (row) as a pair
        for i, row in enumerate(self.board):
            # print row number and rows of "."
            print(f"{i + 1} " + " ".join(row))

# create a new class for the computer's game board, which inherits attributes 
# from the GameBoard class and adds new attributes e.g. hidden from player
class ComputerBoard(GameBoard):   
    def __init__(self, size):
        """
        initialise the ComputerBoard class
        """
        # inherit attributes from GameBoard class
        super().__init__(size) 
        # new attribute - store the computer's board as a hidden version
        self.hidden_board = [["." for _ in range(size)] for _ in range(size)]

    def print_hidden_board(self):
        """
        print the computer's board with the ships hidden to the player
        """
        print("\nThe computer's board.\n")
        print("  " + " ".join([chr(65 + i) for i in range(self.size)]))
        for i, row in enumerate(self.hidden_board):
            # create a new variable that contains an empty list
            hidden_row = []
            # iterate through each cell in each row
            for cell in row:
                # add any cells with "S" to the hidden_row list as "."
                if cell == "S":
                    hidden_row.append(".")
                # add other cells to hidden_row list as 'cell' i.e. "."
                else:
                    hidden_row.append(cell)
            print(f"{i + 1} " + " ".join(hidden_row))


def what_size():
    """
    generate a game board based upon the player's choice
    """
    while True:
        # use 'try' and 'except' statements to catch non-numeric and out of range inputs
        try:
            # player inputs the desired board size
            board_size = input("What size board would you like to use?\nPlease choose a number between 4 and 8: ")

            # attempt to convert the input to an integer
            board_size = int(board_size)

            # check that the integer is within range
            if 4 <= board_size <= 8:
                print("\nOkay, here is your board!\n")

                # store board_size value for later use
                return board_size
            else:
                # if the input is a digit but the integer is out of range, raise an expection
                raise ValueError("\nThe number must be between 5 and 10. Please try again.\n")
        
        except ValueError as e:
            # assign ValueError to an 'e' variable and catch both non-numeric and custom range errors
            print(f"\nInvalid input: {e}. Please try again.\n")

def guess_column(board_size):
    """
    user inputs a column guess
    """
    # store the columm headings based upon board size
    col_headings = [chr(65 + i) for i in range(board_size)]
    while True:
        # input prompt shows the column headings available based upon board size
        guess_col = input(f"\nTarget the computer! Choose a column {" ".join(col_headings)}: ").upper()
        if guess_col == "Q":
            quit()
        if guess_col.isdigit():
            print(f"You chose {guess_col}. Please chose a letter for the column.")
        else:
            if guess_col not in col_headings:
                print("That column does not exist. Please choose a letter within range.")
            else:
                print(f"You selected {guess_col}.")
                return guess_col

def guess_row(board_size, guess_col):
    """
    user inputs a row guess
    """
    while True:
        try:
            # player inputs the desired row based upon board size
            guess_row = input(f"Continue to target! Chhose a row from 1 - {board_size}: ")

            # attemp to convert input to an integer
            guess_row = int(guess_row)

            # check that the integer is within range
            if 1 <= guess_row <= board_size:
                print(f"You targeted {guess_col,{guess_row}}!")
                # store guess_row value for later use
                return guess_row

            else:
                # if the input is a digit but the interger is out of range
                raise ValueError(f"The number must be between 1 and {board_size}")
        except ValueError as e:
            print(f"/nInvalid input: {e}. Please try again.\n")


def main():
    board_size = what_size()
    game = GameBoard(board_size)
    game.print_board()
    computer = ComputerBoard(board_size)
    computer.print_hidden_board()
    col_guess = guess_column(board_size)
    row_guess = guess_row(board_size, col_guess)

welcome()
main()