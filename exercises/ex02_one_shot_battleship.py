"""EX02 - A one-shot battleship."""
__author__ = "730704898"

# Initial variables used to contruct the grid
grid_size: int = 4
secret_row: int = 3  # Secret row/ columns used to check against player input
secret_column: int = 2

# Constants declared to quickly access emoji information and print the grid
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# Gets the user's guess for the row and the column - asks again if it is outside of the grid size range
row_guess: int = int(input("Guess a row: "))
while (row_guess > grid_size or row_guess < 1):
    row_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

column_guess: int = int(input("Guess a column: "))
while (column_guess > grid_size or column_guess < 1):
    column_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

result: str = ""  # Declare a string for the result emoji

if (row_guess == secret_row and column_guess == secret_column):
    result = RED_BOX
else:
    result = WHITE_BOX

row_index: int = 1  # Initializes an index counter for the current row being printed
while (row_index <= grid_size):  # Prints out the number of rows that the grid size dictates. If
    emoji_row: str = ""
    column_index = 1
    if (row_guess == row_index):  # If the row guess is the same as the current row being printed append either red or white to the position of the column index. 
        while (column_index <= grid_size):
            if (column_index == column_guess):
                emoji_row += result
            else:
                emoji_row += BLUE_BOX
            column_index += 1
    else:
        while (column_index <= grid_size):  # Loops through the no. of comlumns and appends the blue box to the row string. Don't know why BLUE_BOX * 4 could not be used. 
            emoji_row += BLUE_BOX
            column_index += 1
    print(emoji_row)
    row_index += 1

# Checks the players row and column guesses and compares them to the secret values - prints hit or miss, but also whether the user has to correct column or row. 
if (row_guess == secret_row):
    if (column_guess == secret_column):
        print("Hit!")
    else:
        print("Close! Correct row, wrong column.")
elif (column_guess == secret_column):
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")