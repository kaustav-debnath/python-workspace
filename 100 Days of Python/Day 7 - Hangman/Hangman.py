word_to_guess = "apple"
print("Welcome to Hangman!")
print(f"Word to Guess: "+"_" * len(word_to_guess))
guessed_letters= []
wrong_guessed_letters = []
guessed_word = ""
length_of_word = len(word_to_guess)
wrong_guesses = 0
while wrong_guesses < 5 and guessed_word != word_to_guess:

    guess = input("Guess a letter: ").lower()

    if guess in word_to_guess:
        guessed_letters.append(guess)
        guessed_word = "".join([letter if letter in guessed_letters else "_" for letter in word_to_guess])  
    else:
        print(f"Sorry, the letter '{guess}' is not in the word.")
        
        wrong_guessed_letters.append(guess)
        wrong_guesses += 1
    if guessed_word == "":
        print("You haven't guessed any letters yet.")
    else:
        print(f"\nCurrent word: {guessed_word}")
    print(f"Wrongly Guessed letters: {wrong_guessed_letters}")
    length_of_word -= 1
    
