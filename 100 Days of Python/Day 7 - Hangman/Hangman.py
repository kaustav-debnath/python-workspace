word_list=['brave', 'dream', 'grace', 'heart', 'light', 'peace', 'truth', 'wisdom', 'wonder', 'faith', 'beauty', 'change', 'circle', 'deeply', 'energy', 'forest', 'gentle', 'humble', 'island', 'kindly', 'balance', 'breathe', 'courage', 'journey', 'harmony', 'passion', 'respect', 'silence', 'triumph', 'welcome', 'brilliant', 'cheerful', 'devotion', 'faithful', 'graceful', 'hopeful', 'laughter', 'peaceful', 'powerful', 'strength']
import random
word_to_guess = random.choice(word_list)
print("Welcome to Hangman!")
# print("Word=>",word_to_guess)
print(f"Word to Guess: "+"_" * len(word_to_guess))
guessed_letters= []
wrong_guessed_letters = []
guessed_word = ""
length_of_word = len(word_to_guess)
wrong_guesses = 0
def draw_hangman(guesses):
    stages = [
         """
           -----
           |   |
           |
           |
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
           |  /|
           |
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
           |  /|\\
           |  /
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           -
        """
        
       
    ]
    return stages[guesses]
def return_guessed_word(word_to_guess, guessed_list):
    placeholder = ""
    for letter in word_to_guess:
        if letter in guessed_list:
            placeholder += letter
        else:
            placeholder += "_"
    # print('placeholder==>',placeholder)
    return placeholder

while wrong_guesses < 6 and guessed_word != word_to_guess:

    guess = input("Guess a letter: ").lower()
    

    if guess in word_to_guess:
        print(f"Your guessed letter '{guess}' is in the word.")
        guessed_letters.append(guess)
        # guessed_word = "".join([letter if letter in guessed_letters else "_" for letter in word_to_guess])  
        guessed_word = return_guessed_word(word_to_guess,guessed_letters)
    else:
        print(f"Sorry, the letter '{guess}' is not in the word.")
        
        wrong_guessed_letters.append(guess)
        wrong_guesses += 1
        print(f"Wrongly Guessed letters: {wrong_guessed_letters} and you have {6 - wrong_guesses} attempts left!")
        print(draw_hangman(wrong_guesses))
    if guessed_word == "":
        print("You haven't guessed any letters yet.")
    elif guessed_word == word_to_guess:
        print(f"\nCongratulations! You've guessed the word: {word_to_guess.upper()}")
        break
    elif wrong_guesses == 6:
        print(f"\nSorry you have lost the game! The correct word was {word_to_guess.upper()}")
        break
    else:
        print(f"\nWord guessed so far: {guessed_word}")
    length_of_word -= 1
    
