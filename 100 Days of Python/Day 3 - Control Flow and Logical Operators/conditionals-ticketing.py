height = int(input("What's your height in cm?"))
bill = 0
if height >= 120:
    print("You are eligible to purchase tickets!")
    age = int(input("What's your age?"))
    if age <= 12:
        bill = 5
        print("Child tickets for $5!")
    elif age <= 18:
        bill = 7
        print("Youth tickets for $7!")
    elif   45 <= age  <= 55:
    # elif age >= 45 and age <= 55:
        bill = 0
        print("Senior Citizen tickets for $0!")
    else:
        bill = 12
        print("Adult tickets for $12!")
    photos_needed = input("Do you require photos to be taken? Please answer Y for Yes and N for No!")
    if photos_needed.upper() == "Y":
        if age < 45 or age > 55:
            bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("You are not eligible to purchase tickets! Please grow taller and then enjoy our ride!")