print("Welcome to the Python Pizza Delivery Service!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni in your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese in your pizza? Y or N: ")

# Small pizza = $15 + pepperoni = $2 
# Medium pizza = $20 + pepperoni = $3
# Large pizza = $25 + pepperoni = $3
# extra cheese = $1

bill = 0

if size.upper() == "S":
    bill += 15
    if pepperoni.upper() == "Y":
        bill += 2

elif size.upper() == "M":
    bill += 20
    if pepperoni.upper() == "Y":
        bill += 3
elif size.upper() == "L":
    bill += 25
    if pepperoni.upper() == "Y":
        bill += 3

else:
    print("You didn't enter the correct size to be ordered!")

if extra_cheese.upper() == "Y":
    bill += 1
    
print(f"Your final bill amount is: ${bill}")