from art import logo
import random
print(logo)

print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100.")

difficulty_level=input("Choose a Difficulty Level. Type 'e' for 'easy' or 'h' for 'hard':\t")
if difficulty_level == "e":
    NUMBER_OF_ATTEMPTS = 10
else:
    NUMBER_OF_ATTEMPTS = 5

CHOSEN_RANDOM_NUMBER = random.randint(1,100)

def play_game(chosen_number, attempts):
    while not attempts == 0:
        user_input = int(input(f"You have {attempts} attempts remaining to guess the number\nMake a guess:\t"))
        if user_input == chosen_number:
            print(f"You got it! The answer was {chosen_number}")
            return
        elif attempts == 1 and user_input != chosen_number:
            print("You have exhausted all your attempts! You lose")
            return
        elif user_input < chosen_number:
            print("Too Low.\nGuess Again:\t")
        elif user_input > chosen_number:
            print("Too High.\nGuess Again:\t")
        attempts -= 1
        
play_game(CHOSEN_RANDOM_NUMBER, NUMBER_OF_ATTEMPTS)