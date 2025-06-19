word_list=['brave', 'dream', 'grace', 'heart', 'light', 'peace', 'truth', 'wisdom', 'wonder', 'faith', 'beauty', 'change', 'circle', 'deeply', 'energy', 'forest', 'gentle', 'humble', 'island', 'kindly', 'balance', 'breathe', 'courage', 'journey', 'harmony', 'passion', 'respect', 'silence', 'triumph', 'welcome', 'brilliant', 'cheerful', 'devotion', 'faithful', 'graceful', 'hopeful', 'laughter', 'peaceful', 'powerful', 'strength']
import random
word_to_guess = random.choice(word_list)
print("Welcome to Hangman!")



stages = [
     """
        -----
        |   |
        |   O
        |  /|\\
        |  / \\
        -
    """,    
    """
        -----
        |   |
        |   O
        |  /|\\
        |  /
        -
    """,
    """
        -----
        |   |
        |   O
        |  /|\\
        |
        -
    """,
    
    """
        -----
        |   |
        |   O
        |  /|
        |
        -
    """,
    """
        -----
        |   |
        |   O
        |   |
        |
        -
    """,
    
    """
        -----
        |   |
        |   O
        |
        |
        -
    """,
    
    
    
    
    
   

]
unguessed_word = "_" * len(word_to_guess)
print(f"Word to Guess:{word_to_guess}\t{unguessed_word}")


lives = 6
game_over = False
correct_guesses = []


while not game_over:
    display = ""
    guess = input("Guess a letter from the word:\t")
    for letter in word_to_guess:
        if letter == guess:
            correct_guesses.append(letter)
            display += letter
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_"
    if guess not in word_to_guess:
        print(f"You Guessed {guess}, that's a wrong guess, so you lose a life!")
        lives -= 1
        if lives == 0:
            game_over = True
            print("Game Over, You Lose!")
    print(f"Guessed Word:\t{display}")
    print(f"You have {lives} attempts left!\n{stages[lives]}")

    if "_" not in display:
        game_over = True
        print("You Win!")

