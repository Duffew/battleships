# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# define constants

def welcome():
    print("\nWelcome to Battleships!\n")
    # while loop runs until player provides a valid input
    while True:
        # provides player input field and converts text to lowercase to match the checks below
        game = input("Would you like to play a game? ('y'/'n'): ").lower()
        if game == "n":
            print("Maybe another time. Goodbye!")
            quit()
        if game == "y":
            print("\nLet's play\n")
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
            if 5 <= board_size <= 1:
                print("\nOkay, here is your board!")
                # store board_size value for later use
                return board_size


welcome()
game = GameBoard(5)
game.print_board()
