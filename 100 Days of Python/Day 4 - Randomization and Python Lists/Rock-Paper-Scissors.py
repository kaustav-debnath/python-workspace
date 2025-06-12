rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = input("Enter your choice for Rock,Paper and Scissors: ").lower()
if player_choice == 'rock':
    player_actual_choice = rock
elif player_choice == 'paper':
    player_actual_choice = paper
elif player_choice == 'scissors':
    player_actual_choice = scissors
else:
    print("Invalid choice")
    exit()
import random
game_vars = [rock, paper, scissors]
system_choice = random.choice(game_vars)

if system_choice == player_actual_choice:
    print(f"You chose {player_actual_choice}")
    print(f"System chose {system_choice}")
    print("Its a Draw!")
elif system_choice == rock and player_actual_choice == scissors:
    print(f"You chose {player_actual_choice}")
    print(f"System chose {system_choice}")
    print("You lose!")
elif system_choice == scissors and player_actual_choice == paper:
    print(f"You chose {player_actual_choice}")
    print(f"System chose {system_choice}")
    print("You lose!")
elif system_choice == paper and player_actual_choice == rock:
    print(f"You chose {player_actual_choice}")
    print(f"System chose {system_choice}")
    print("You lose!")
else:
    print(f"You chose {player_actual_choice}")
    print(f"System chose {system_choice}")
    print("You win!")