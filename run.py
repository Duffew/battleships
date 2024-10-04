
# python module for generating random integers
import random

# global variables
player_turns = 0
computer_turns = 0
previous_player_targets = []
previous_computer_targets = []
player_ships_remaining = 0
computer_ships_remaining = 0


def welcome():
    """
    Provide a welcome message before the game begins
    """
    print("\nWelcome to Battleships!\n")
    # while loop runs until player provides a valid input
    while True:
        # provides player input field and converts text to lowercase to match
        # the checks below
        game = input("Would you like to play a game? (y/n): \n").lower()
        if game == "n":
            print("Maybe another time. Goodbye!")
            quit()
        if game == "y":
            print("\nLet's play!\n")
            break
        else:
            print("That is not a valid input. Please try again.")
            continue


# create a class for the game board
class GameBoard:
    def __init__(self, size):
        """
        Initialise the GameBoard class
        """
        # define the GameBoard attributes
        # the GameBoard has a size (player defined)
        self.size = size

        # the GameBoard board is a list of x, y coordinates
        #  with a range of sizes
        self.board = [["." for x in range(size)] for y in range(size)]

        # the GameBoard has a total number of cells
        self.total_cells = size * size

        # 20% of the GameBoard cells are ships
        self.num_ships = (self.total_cells * 20) // 100

        # ships are placed randomly on the GameBoard when this method is called
        self.place_random_ships()

    def place_random_ships(self):
        """
        place ships randomly on the board
        """
        # create a list of all possible coordinates
        all_coordinates = [
            (x, y) for x in range(self.size)
            for y in range(self.size)
        ]

        # randomly choose ship positions from the all_coordinates list
        ship_positions = random.sample(all_coordinates, self.num_ships)

        # itertae ship placement using "S" to represent ships
        for x, y in ship_positions:
            self.board[x][y] = "S"

    def print_board(self):
        """
        Print the GameBoard
        """
        # iterate column headers A - ? begin with a double space for alignment
        # chr(65 + i): indexing begins with capital 'A'
        # (65th character in ASCII)
        print("  " + " ".join([chr(65 + i) for i in range(self.size)]))

        # use enumerate() to return row index (i) and row content (row) as pair
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
        print("\nHere is the computer's board.\n")
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
    generate a game board based upon the player's choice of board size
    """
    while True:
        # use try and except to catch non-numeric and out of range inputs
        try:
            # player inputs the desired board size
            size_board = "What size board would you like to use?\n"
            choose = "Please choose a number betwen 4 and 8: \n"
            board_size = input(f"{size_board}{choose}")

            # attempt to convert the input to an integer
            board_size = int(board_size)

            # check that the integer is within range
            if 3 <= board_size <= 8:
                print("\nOkay, here is your board. (S = ship)\n")

                # store board_size value for later use
                return board_size
            else:
                # if the input is a digit but the integer is out of range,
                # raise an expection
                raise ValueError("\nThe number must be between 3 and 8.\n")
        except ValueError as e:
            # assign ValueError to an 'e' variable and catch both non-numeric
            # and custom range errors
            print(f"\nInvalid input: {e}Please try again.\n")


def game_setup():
    """
    set up the player's and computer's board
    based upon player's chosen board size
    """
    board_size = what_size()

    player_board = GameBoard(board_size)
    player_board.print_board()

    computer_board = ComputerBoard(board_size)
    computer_board.print_hidden_board()

    global player_ships_remaining
    global computer_ships_remaining

    # get the starting number of ships for the player and the computer
    player_ships_remaining = player_board.num_ships
    computer_ships_remaining = computer_board.num_ships

    input("\nThe boards are set. Press 'Enter' to begin the game...")
    # store values for use in the play_game() function below
    return player_board, computer_board, board_size


def player_guess_column(board_size):
    """
    user inputs a column guess - makes use of the returned board_size value
    """
    # store the column headings based upon board size
    col_headings = [chr(65 + i) for i in range(board_size)]
    while True:
        # input text shows the column headings available based upon board size
        choose = "\nTarget the computer. Choose a column from "
        out = " or Q to quit: \n"
        column_guess = input(f"{choose}{" ".join(col_headings)}{out}").upper()
        if column_guess == "Q":
            quit()
        if column_guess.isdigit():
            letter = "Please choose a letter for the column."
            print(f"You chose {column_guess}. {letter}")
        elif column_guess not in col_headings:
            again = "Please choose a column within range."
            print(f"That column is not available. {again}")
        else:
            print(f"You selected column {column_guess}.")
            return column_guess


# takes (makes use of) data stored in the board_size and column_guess variables
def player_guess_row(board_size, column_guess):
    """
    user inputs a row guess

    """
    while True:
        try:
            # player inputs the desired row
            cont = "\nContinue to target! Choose a row from 1 - "
            row_guess = input(f"{cont} {board_size}: \n")

            # attempt to convert the input to an integer
            row_guess = int(row_guess)

            # check that the integer is within range
            if 1 <= row_guess <= board_size:
                print(f"You targeted {column_guess}{row_guess}.\n")
                # store row_guess value for later use
                return row_guess
            else:
                # if the input is a digit but the integer is
                # out of range, raise an expection
                raise ValueError(f"Choose be between 1 and {board_size}")
        except ValueError as e:
            print(f"\nInvalid input: {e}. Please try again.\n")


def player_turn(computer_board, board_size):
    """
    manage the user's turn once a guess has been made
    """

    # instruct python to use global variables
    global player_turns
    global computer_ships_remaining
    global previous_player_targets

    while True:
        # get player's column guess
        column_guess = player_guess_column(board_size)

        # get player's row guess using column guess
        row_guess = player_guess_row(board_size, column_guess)

        # combine column and row guesses
        target = f"{column_guess}{row_guess}"

        # check that this turn's coordinates haven't already been guessed
        if target in previous_player_targets:
            again = "Please choose another target."
            print(f"You already targeted {target}. {again}")
            continue

        # use ord() to convert the guessed column heading BACK into
        # its index reference - ASCII 'A' = 65
        col_index = ord(column_guess) - 65

        # check the computer's board for a hit
        if computer_board.board[row_guess - 1][col_index] == "S":

            # decrement the computer's ships for a hit
            computer_ships_remaining -= 1

            # check for how many ships the computer has remaining and use
            # 'ship' or 'ships' in print message
            how_many = "ship" if computer_ships_remaining == 1 else "ships"
            print(
                f"You sank a ship at {target}! The computer has "
                f"{computer_ships_remaining} {how_many} remaining!"
                )

            # update the computer's board with player's guess after a hit
            computer_board.hidden_board[row_guess - 1][col_index] = "!"
        else:
            # check for how many ships the computer has remaining and use
            # 'ship' or 'ships' in print message after a miss
            how_many = "ship" if computer_ships_remaining == 1 else "ships"
            print(
                f"Miss! No ship at {target}. The computer has "
                f"{computer_ships_remaining} {how_many} remaining."
                )

            # update the computer's board with player's guess after a miss
            computer_board.hidden_board[row_guess - 1][col_index] = "O"

        # update list of player's previous targets
        previous_player_targets.append(target)

        # reprint the computer's hidden board
        computer_board.print_hidden_board()

        # increment the players number of turns
        player_turns += 1

        # exit the loop after a valid guess
        break

    # check for a possible player win
    if computer_ships_remaining == 0:
        print(f"\nYou sank all the computer's ships in {player_turns} turns!")
        print("Allow the computer to take its final turn...")


def computer_turn(player_board, board_size):
    """
    Manage the computer's turn.
    """
    # instruct python to use global variables
    global computer_turns
    global player_ships_remaining
    global previous_computer_targets

    while True:
        # store random integers between 0 and
        # the board size minus 1 for the columns and rows
        column_index = random.randint(0, board_size - 1)
        row_index = random.randint(0, board_size - 1)

        # check that this target has not been used previously
        if (row_index, column_index) not in previous_computer_targets:
            previous_computer_targets.append((row_index, column_index))

            # check to see if the computer sank a player ship
            if player_board.board[row_index][column_index] == "S":

                # decrement player's ships after a hit
                player_ships_remaining -= 1

                # update the player's board for a computer hit
                player_board.board[row_index][column_index] = "!"

                # if player's last ship is sunk
                if player_ships_remaining == 0:
                    print(
                        f"The computer sank your last ship at "
                        f"{chr(65 + column_index)}{row_index + 1}! "
                        f"You have no ships remaining!\n"
                    )
                    break
                else:
                    # check for how many ships the player has remaining after
                    # a hit and use 'ship' or 'ships' in the print message
                    how_many = (
                        "ship"
                        if player_ships_remaining == 1
                        else "ships"
                    )

                    print(
                        f"The computer sank your ship at "
                        f"{chr(65 + column_index)}{row_index + 1}! "
                        f"You have {player_ships_remaining} {how_many} "
                        f"remaining!"
                    )
            else:
                # update the player's board for a computer miss
                player_board.board[row_index][column_index] = "O"

                # check for how many ships the player has remaining after
                # a miss and use 'ship' or 'ships' in print message
                how_many = "ship" if player_ships_remaining == 1 else "ships"
                print(
                    f"The computer missed at {chr(65 + column_index)}"
                    f"{row_index + 1}. You have {player_ships_remaining} "
                    f"{how_many} remaining."
                )

            # print the updated player board
            print("\nHere is your board.\n")
            player_board.print_board()

            # increment the computer's turn tally
            computer_turns += 1

            # exit the loop after a valid guess
            break


def play_game():
    """
    Alternates turns between the player and the computer.
    Manage win conditions
    """
    global player_turns
    global computer_turns

    # unpack the values returned by the game_setup() function
    player_board, computer_board, board_size = game_setup()

    # Main game loop
    while True:
        print("\nYour Turn.")
        input("Press 'Enter' to make a guess ('!' = 'Sink', 'O' = 'Miss').")
        # call player's turn function
        computer_board.print_hidden_board()
        player_turn(computer_board, board_size)

        # check that the player has the potential to win
        # before the computer plays its turn
        if computer_ships_remaining == 0:
            # Allow the computer to take its final turn
            input("\nPress 'Enter' to see the computer's final turn...\n")
            print("Computer's Turn.")

            # call computer turn function
            computer_turn(player_board, board_size)

            # check for a draw after the computer's final turn
            if player_ships_remaining == 0:
                print("\nIt's a draw! Game Over!\n")
            else:
                print(
                    f"\nThe computer couldn't sink all your ships! "
                    f"You won the game in {player_turns} turns! Game Over!\n"
                )
            break

        # allow the player to control the computer's turn
        #  by hitting 'Enter' when ready
        input("\nPress 'Enter' to see the computer's turn...")

        print("\nComputer's Turn")
        computer_turn(player_board, board_size)

        # Check if the computer has won after its turn
        if player_ships_remaining == 0:
            player_board.print_board()
            computer_turns += 1
            print(
                f"\nThe computer sank all your ships in {computer_turns} "
                f"turns! Better luck next time! Game Over!\n"
            )
            break


welcome()
play_game()
