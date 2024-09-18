# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# define constants
COLUMNS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
ROWS = range(1, 9)

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


welcome()
game = GameBoard(5)
game.print_board()
