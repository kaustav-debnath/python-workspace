from art import logo
import random




def calculate_scores(user_cards, computer_cards):
    """
    :param user_cards:
    :param computer_cards:
    :return: final_score: a dict of user and computer final score
    """
    user_sum = 0
    computer_sum = 0
    user_ace_count = 0
    comp_ace_count = 0
    for val in user_cards:
        if val == 11:
            user_ace_count += 1
        user_sum += val
    # print(user_ace_count)
    if user_sum > 21 and user_ace_count > 0:
        for i in range(0,user_ace_count):
            user_sum -= 10
    for val in computer_cards:
        if val == 11:
            comp_ace_count += 1
        computer_sum += val
    # print(comp_ace_count)
    if computer_sum > 21 and comp_ace_count > 0:
        for i in range(0,comp_ace_count):
            computer_sum -= 10
    score = {
        "user_score": user_sum,
        "computer_score": computer_sum
    }
    # print(f"user_sum:\t{user_sum}, computer_sum:\t{computer_sum}")
    return score
def print_final_standing(user, comp):
    if user > 21:
        print("You went over, You lose! 😒")
    elif user <= 21 and user == comp:
        print("Its a Draw!")
    elif (user <= 21
          and comp <= 21
          and user < comp):
        print("You went over, You lose! 😒")
    else:
        print("You win! 😊 ")
def print_scores(user_cards, computer_cards, score, initial=False):
    """
    :param user_cards:
    :param computer_cards:
    :param score:
    :param initial: this input prints only first time
    :return: no return just print the right message
    """
    if initial:
        print(f"Your cards:\t{user_cards}, current score:\t{score['user_score']}")
        print(f"Computer's first card: \t{computer_cards[0]}")
        return
    
    print(f"Your cards:\t{user_cards}, current score:\t{score['user_score']}")
    print(f"Computer's cards: \t{computer_cards}, Computer's final score:\t{score['computer_score']}")
def print_logo():
    print(logo)
def play_black_jack():
    
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_dealt_cards = []
    computer_dealt_cards = []

    user_choice_to_play = input("Do you want to play a game of black jack? Type 'y' or 'n':\t")    
    selected_to_play=True

    if user_choice_to_play == "y":
        print("\n"*20)
        print_logo()
        selected_to_play = True
        user_dealt_cards = random.choices(cards, k=2)
        computer_dealt_cards = random.choices(cards, k=3)
    else:
        return


    final_score_dict = calculate_scores(user_dealt_cards, computer_dealt_cards)

    if final_score_dict["user_score"] > 21:
        print_scores(user_dealt_cards, computer_dealt_cards, final_score_dict, False)
    else:
        print_scores(user_dealt_cards, computer_dealt_cards, final_score_dict, True)

    while selected_to_play:
        continue_dealing = input("Type 'y' to get another card or 'n' to pass:\t")
        
        if continue_dealing == "y":
            user_dealt_cards.append(random.choice(cards))
            final_score_dict = calculate_scores(user_dealt_cards, computer_dealt_cards)
            print_scores(user_dealt_cards, computer_dealt_cards, final_score_dict, True)
            if final_score_dict["user_score"] > 21:
                print_final_standing(final_score_dict["user_score"], final_score_dict["computer_score"])
                selected_to_play = False
                play_black_jack()
        else:
            print_scores(user_dealt_cards, computer_dealt_cards, final_score_dict, False)
            print_final_standing(final_score_dict["user_score"], final_score_dict["computer_score"])
            selected_to_play = False
            play_black_jack()
    
play_black_jack()



