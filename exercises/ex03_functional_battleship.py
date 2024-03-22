"""EX03 - A battleship that can be played 5 times."""

import random
__author__ = "730704898"


BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(grid_size: int, row_or_column: str) -> int:
    """Allows the player to input guesses for rows and columns within the grid size."""
    assert row_or_column == "row" or row_or_column == "column"
    user_guess: int
    if row_or_column == "row":
        user_guess = int(input("Guess a row: "))
    else:
        user_guess = int(input("Guess a column: "))

    while user_guess < 1 or user_guess > grid_size:
        user_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

    return user_guess


def print_grid(grid_size: int, row_guess: int, column_guess: int, is_correct: bool) -> None: 
    """Prints the grid based on the grid size and player input."""
    i: int = 0
    box_color: str = ""
    #  Changes the printed box to white or red based on whether the guess is correct.
    if is_correct:
        box_color = RED_BOX
    else:
        box_color = WHITE_BOX

    #  If the player row guess is the current row being printed, loop through and print white or red at the correct column. Otherwise print an entire row of blue boxes.
    while i < grid_size:
        if i + 1 == row_guess:
            j: int = 0
            row_str: str = ""
            while j < grid_size:
                if j + 1 == column_guess:
                    row_str += box_color
                else:
                    row_str += BLUE_BOX
                j += 1
            print(row_str)
        else:
            print(BLUE_BOX * grid_size)
        i += 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Compares the user's guess to the secret values and evaluates to true or false."""
    if row_guess == secret_row and column_guess == secret_column:
        return True
    return False


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Main function which controls the game loop."""
    has_won: bool = False
    max_turns: int = 5
    current_turn: int = 1
    #  Game loop for program.
    while current_turn < max_turns + 1 and not has_won:
        print(f"=== Turn {current_turn}/{max_turns} ===")
        row_guess: int = input_guess(grid_size, "row")
        column_guess: int = input_guess(grid_size, "column")
        correct: bool = correct_guess(secret_row, secret_column, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, correct)
        if not correct:
            print("Miss!")
            current_turn += 1
        else:
            print("Hit!")
            has_won = True
    if has_won: 
        print(f"You won in {current_turn}/{max_turns} turns!")
    else:
        print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))