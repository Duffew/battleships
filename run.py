# Your code goes here.
# You can delete these comments, but do not change the name of this file
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
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.total_cells = size * size
        self.num_ships = (self.total_cells * 20) // 100 # ships are 20% of the total cells on the board
        self.place_random_ships() # method to randomly place the ships on the board

    def place_random_ships(self):
        """
        place ships randomly on the board
        """
        #create a list of all possible coordinates
        all_coordinates = [(x, y) for x in range(self.size) for y in range(self.size)]
        # randomly choose ship positions from the all_coordinates list
        ship_positions = random.sample(all_coordinates, self.num_ships)

        #itertae ship placement using "S" to represent ships
        for x, y in ship_positions:
            self.board[x][x] = "S"

    def print_board(self):
        """
        Print the GameBoard
        """
        # print column headers A - ? - use list comprehension to iterate
        print("  " + " ".join([chr(65 + i) for i in range(self.size)]))
        for i, row in enumerate(self.board):
            # print row number and rows of "."
            print(f"{i} " + " ".join(row))

def what_size():
    """
    generate a game board based upon the player's choice
    """
    while True:
        # define the board_size variable
        board_size = input("What size board would you like to use?\nPlease choose a nuumber between 5 and 10: ")
        # check that the input is a digit
        if board_size.isdigit():
            # if True, convert the string to an integer
            board_size = int(board_size)
            # check that the integer is within range
            if 5 <= board_size <= 10:
                print("\nOkay, here is your board!\n")
                # store board_size value for later use
                return board_size
            else:
                # if the input is a digit but the integer is out of range
                print("\nThe number must be between 5 and 10. Please try again.\n")
        else:
            # if the input is not a digit
            print("\nThat is not a number. Please try again.\n")

def main():
    board_size = what_size()
    game = GameBoard(board_size)
    game.print_board()

welcome()
main()
