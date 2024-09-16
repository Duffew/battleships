# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# define constants
COLUMNS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
ROWS = range(1, 9)

def generate_grid():
    print("\nWelcome to Battleships!\n")
    # while loop runs until player provides a valid input
    while True:
        # provides player input field and converts text to lowercase to match the checks below
        game = input("Would you like to play a game? ('y'/'n')").lower()
        if game == "n":
            print("Maybe another time. Goodbye!")
            quit()
        if game == "y":
            print("\nLet's play\n")
            break
        else:
            print("That is not a valid input. Please try again.")
            continue

    # print the column headers A - H
    print("   " + "  ".join(COLUMNS)) 
    # print each row beginning with row numbers
    for row in ROWS: 
        # print the row number and '.' for each column in the row
        grid = print(f"{row}  " + "  ".join(["."] * len(COLUMNS)))
    return grid

generate_grid()