print('''\n

888                                                          
888                                                          
888                                                          
888888 888d888 .d88b.   8888b.  .d8888b  888  88 8888d888 .d88b.  
888    888P"  d8P  Y8b     "88b 88K      888  88 8888P"  d8P  Y8b 
888    888    88888888 .d888888 "Y8888b. 888  88 8888    88888888 
Y88b.  888    Y8b.     888  888      X88 Y88b 88 8888    Y8b.     
 "Y888 888     "Y8888  "Y888888  88888P'  "Y8888 8888     "Y8888  
      
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
      
''')

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


