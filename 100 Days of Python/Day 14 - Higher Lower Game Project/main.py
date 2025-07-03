from art import logo, vs
from game_data import data
import random
print(logo)

USER_SCORE = 0
DID_USER_WIN = True
def fetch_game_data(game_data,current_user):
    """
    fetches random data from the game data and compares it with the current user data already fetched
    """
    valid_random = 0
    random_choice = {}
    if current_user == {}:
        return random.choice(game_data)
    else:
        while valid_random < 1:
            random_choice = random.choice(game_data)
            if  random_choice['name']!= current_user['name']:
                valid_random += 1
    return random_choice

def compare_users(user1, user2):
    """
    compares 2 users based on their follower count
    """
    if user1['follower_count'] > user2['follower_count']:
        return user1
    else:
        return user2
def check_user_response(user_choice, choice_a, choice_b, winner):
    """
    checks if the user's choise is correct and returns true if user selection is correct and false otherwise
    """
    global USER_SCORE
    if user_choice == 'A' and winner['name'] == choice_a['name']:
        USER_SCORE += 1
        return True
    elif user_choice == 'B' and winner['name'] == choice_b['name']:
        USER_SCORE += 1
        return True
    else:
        return False

def play_game():
    """
    Main function to play the game, it fetches random data and compares it with the user input
    """
    global USER_SCORE
    global DID_USER_WIN
    random_choice_a = fetch_game_data(data,{})

    while DID_USER_WIN:
        random_choice_b = fetch_game_data(data, random_choice_a)
        print(f"Compare A: {random_choice_a['name']},a {random_choice_a['description']}, from {random_choice_a['country']}")
        print(vs)
        print(f"Compare B: {random_choice_b['name']},a {random_choice_b['description']}, from {random_choice_b['country']}")
        user_choice = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
        winning_user = compare_users(random_choice_a, random_choice_b)
        DID_USER_WIN = check_user_response(user_choice, random_choice_a, random_choice_b, winning_user)
        if DID_USER_WIN:
            print(f"You Win! Current Score: {USER_SCORE}")
            random_choice_a = random_choice_b
    print(f"You Lose!: Your Final Score: {USER_SCORE}")
play_game()