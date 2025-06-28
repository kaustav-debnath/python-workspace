from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


input1 = input("Enter the first number:\t")
condition_show = True

while condition_show:

    operator = input("Enter a math operator +,-,* or / :\t")
    input2 = input("Enter the next number:\t")
    result = operations[operator](float(input1), float(input2))
    print(f"The result of {input1} {operator} {input2} : {result}")
    user_choice = input("Do you wish to continue Type yes or no:\t")
    if user_choice == "yes":
        condition_show = True
        input1 = result
    else:
        condition_show = False

