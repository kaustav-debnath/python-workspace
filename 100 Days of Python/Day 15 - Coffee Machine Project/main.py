from resource import MENU, resources
import math
profit = 0
def is_sufficient_resources(ingredients, resource):
    for item in ingredients:
        if resource[item] < ingredients[item]:
            print(f"Sorry there is not enough {item} available")
            return False
    return True
def process_coins(drink):
    print(f"Please insert the coins for your {drink} cost: {MENU[drink]['cost']}")
    coin_value = int(input("Please insert the number of Quarters: ")) * 0.25
    coin_value += int(input("Please insert the number of Dimes: ")) * 0.1
    coin_value += int(input("Please insert the number of Nickels: ")) * 0.05
    coin_value += int(input("Please insert the number of Quarters: ")) * 0.01
    return coin_value
def calculate_coins_to_return(cost, paid_amount):
    if paid_amount < cost:
        print("Sorry that's not enough money. Money refunded. ")
        return False
    else:
        round_off_amount = round(paid_amount - cost,2)
        print(f"Here is {round_off_amount} dollars in change.")
        resources["Money"] += cost
        return True
def make_coffee(ingredients, resource):
    for item in ingredients:
        resource[item] -= ingredients[item]


machine_is_on = True

while machine_is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        print("Coffee machine is shutting down")
        machine_is_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif not user_choice.lower() == "espresso" and not user_choice.lower() == "latte" and not user_choice.lower() == "cappuccino":
        print("Please enter correct drink choice")
    else:
        if is_sufficient_resources(MENU[user_choice]["ingredients"],resources):
            payment = process_coins(user_choice)
            if calculate_coins_to_return(MENU[user_choice]["cost"], payment):
                make_coffee(MENU[user_choice]["ingredients"],resources)
                profit += MENU[user_choice]["cost"]
