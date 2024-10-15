# 1. The Calculator App
# Objective: The aim of this assignment is to 
# build a basic calculator that can perform addition, 
# subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.

# Task 2: Use inputs to ask the user what operation they want to perform, 
# and what numbers they want to use.

# Task 3: Ensure your code can handle division by zero and 
# other potential errors. So if you divide by 0, there is 
# error handling set up to prevent an error from showing in the console.

# This function will add the 2 numbers together
def add(num1 , num2):
    total = num1 + num2
    print(f"The total of the two numbers is {total}.")

# This function will subtract number 2 from number 1
def subtract(num1, num2):
    difference = num1 - num2
    print(f"The difference between the two numbers is {difference}")

def multiply(num1, num2):
    product = num1 * num2
    print(f"The product of the two numbers is {product}.")

def divide(num1, num2):
    quotient = num1 / num2
    print(f"The quotient is {quotient}.")

# Defined reusable questions to short keystrokes throughout conditionals
num1_quest = 'What is the first number? '
num2_quest = 'What is the second number? '

# Set a while loop so the user can keep going until they decide to quit
while True:
    selection = input("What would you like to do [A]dd, [S]ubtract, [M]ultiply, [D]ivide or [Q]uit?\n").upper()
    if selection == 'A':
        num1 = int(input(num1_quest))
        num2 = int(input(num2_quest))
        add(num1, num2)
    elif selection == 'S':
        # The print line was added to make sure the user knew which order these would go.
        print('This will subtract your second number from your first number.')
        num1 = int(input(num1_quest))
        num2 = int(input(num2_quest))
        subtract(num1, num2)
    elif selection == 'M':
        num1 = int(input(num1_quest))
        num2 = int(input(num2_quest))
        multiply(num1, num2)
    elif selection == 'D':
        num1 = int(input(num1_quest))
        num2 = int(input(num2_quest))
        # Used a try and except block to prevent the program from crashing and let the user know they
        # cannot divide by zero.
        try:
            divide(num1, num2)
        except ZeroDivisionError:
            print('Cannot divide by Zero!')
    elif selection == 'Q':
        break
    else:
        print('Invalid selection. Please try again.')
