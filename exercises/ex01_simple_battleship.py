"""EX01 - A Simple Battleship."""

__author__ = "730704898"

result: str = ""

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


player1_input: int = int(input("Pick a secret boat location between 1 and 4: "))
if (player1_input < 1):
    print("Error! " + str(player1_input) + " too low!")
    exit()
if (player1_input > 4):
    print("Error! " + str(player1_input) + " too high!")
    exit()

player2_input: int = int(input("Guess a number between 1 and 4: "))
if (player2_input < 1):
    print("Error! " + str(player2_input) + " too low!")
    exit()
if (player2_input > 4):
    print("Error! " + str(player2_input) + " too high!")
    exit()

if (player2_input == player1_input):
    result = RED_BOX
    print("Correct! You hit the ship.")
else:
    result = WHITE_BOX
    print("Incorrect! You missed the ship.")

total: str = ""

for x in range(4):
    if (x + 1 == player2_input):
        total += result
    else:
        total += BLUE_BOX
print(total)
     