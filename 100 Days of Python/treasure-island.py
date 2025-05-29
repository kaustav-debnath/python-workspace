print("Welcome to the Treasure Island! Your mission is to find the treasure.") 
crossroad = input("You are at a crossroad. Do you want to go left or right? (L/R): ").upper()
if crossroad == "R":
    print("You fell into a hole. Game Over!")
elif crossroad == "L":
    swim_or_wait = input("You come to a lake. Do you want to swim across or wait for a boat? (S/W): ").upper()
    if swim_or_wait == "S":
        print("You were attacked by a trout. Game Over!")
    elif swim_or_wait == "W":
        door = input("You arrive at a house with three doors. One red, one yellow and one blue. Which door do you want to open? (R/Y/B): ").upper()
        if door == "R":
            print("It's a room full of fire. Game Over!")
        elif door == "Y":
            print("You found the treasure! You Win!")
        elif door == "B":
            print("You enter a room of beasts. Game Over!")
        else:
            print("You didn't choose a valid door. Game Over!")
    else:
        print("You didn't choose a valid option. Game Over!")
else:
    print("You didn't choose a valid option. Game Over!")
# The code implements a simple text-based adventure game where the player makes choices to find a treasure.
# The player can choose to go left or right, swim or wait, and select a door to open.           
# Depending on the choices made, the player may win or lose the game.
# The game ends with either a win or a game over message based on the player's decisions.


