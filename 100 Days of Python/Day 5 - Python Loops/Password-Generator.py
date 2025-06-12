letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random
password = []
# for letter in random.sample(letters, nr_letters):
#     password.append(letter)
# for symbol in random.sample(symbols, nr_symbols):
#     password.append(symbol)
# for number in random.sample(numbers, nr_numbers):
#     password.append(number)

for char in range(0,nr_letters):
    password.append(random.choice(letters))
for sym in range(0,nr_symbols):
    password.append(random.choice(symbols))
for num in range(0,nr_numbers):
    password.append(random.choice(numbers))

# print(password)
# Use random.shuffle to shuffle the contents of the password list
random.shuffle(password)
# password = ''.join(password)
final_password = ""
# for loop to concatenate the chars from the password list into final_password string
for char in password:
    final_password += char
print(f'Your password is: {final_password}')


