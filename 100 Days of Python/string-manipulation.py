text = 'Hello World\n'

# Using string manipulation printing the text 3 times
print(text*3) 

# Using string manipulation to concatenate User input and print the output with prefix and suffix concatenation
print("Hello "+input("What's your name?")+"!")

# Using string manipulation by storing the user input into a variable and then manipulating the overall output
inputText = input("What's your name?")
inputLength = len(inputText)
print("Username: Hello "+ inputText + "\nLength of user input: "+str(inputLength))


#Wrapping everything into a single step
print(len(input("What's your name?")))