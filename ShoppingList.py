# 2. The Shopping List Maker
# Objective: The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.

# Task 2: Include a function to remove items from the list.

# Task 3: Add a function that prints out the entire list in a formatted way.

# Note: The goal of this is to be a program. The recommendation is to use a 
# while loop that will allow the user to continue to add, remove, and print off 
# their shopping list until they decide to "quit", also known as breaking the loop.

# Create an empty list for the user to manipulate
shopping_list = []

# Function to append item to the shopping list array
def add_item():
    global shopping_list
    item = input('What would you like to add to your shopping list? \n')
    shopping_list.append(item)

# Function to remove item from the shopping list
def remove_item():
    global shopping_list
    to_remove = input('What item would you like to remove? \n')
    shopping_list.remove(to_remove)

# Function to print the current list
def print_list():
    global shopping_list
    print("Here is your list: ")
    for item in shopping_list:
        print(item)

# Set a while loop to continue running the program until the user decides to quit
while True:
    selection = input('Please make your selection. [A]dd to list, [R]emove from list, [P]rint list, or [Q]uit program.').upper()

# Conditionals to activate based on user selection
    if selection == 'A':
        add_item()
    elif selection == 'R':
        remove_item()
    elif selection == 'P':
        print_list()
    elif selection == 'Q':
        break
    else:
        print('Invalid selection, please try again.')
