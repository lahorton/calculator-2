"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


print("Welcome to our calculator")


def menu():
    """prints the menu of actions"""
    print("Add: enter 'A'")
    print("Subtract: enter 'S'")
    print("Multiply: enter 'M'")
    print("Divide: enter 'D'")
    print("Square: enter 'SQ'")
    print("Cube: enter 'C'")
    print("Remainder: enter 'R'")
    print("Square Root: enter 'SR'")
    print("Power: enter 'P'")
    print("Quit: enter 'Q'")


def get_input():
    """Get's initial user input and tokenizes."""
    menu()
    numbers = input("Enter action, with operator first. i.e. A 2 3. \n: ")
    numbers = numbers.rstrip()
    tokens = numbers.split(" ")
    return tokens


def check_input(tokens):
    """Checking user input for correct type and format."""
    while True:
        if tokens[0].isalpha():
            # if tokens[0].lower() == "q":
            #     print("You think you can calculate on your own?!!")
            #     sure = input("Are you sure you want to quit? Y/N").lower()
            #     if sure == "n":
            #         get_input()
            #     else:
            #         break
            for num in tokens[1:]:
                if num.isdigit():
                    return False
                else:
                    print("Please type digits aka 1, -4, 1000.")
                    get_input()
        else:
            print("Please choose action from the menu.")
            menu()
            get_input()

    print("Excellent, let me think for a moment...")


def convert_to_floats(tokens):
    """converts list of strings that are numbers to floats"""
    float_tokens = []
    for num in tokens:
        if num.isdigit():
            num = float(num)
            float_tokens.append(num)
        else:
            float_tokens.append(num)
    return float_tokens


def call_arithmetic(tokens):
    """Based off of user input performs action."""
    if tokens[0] == "A":
        print(add(tokens[1], tokens[2]))
    if tokens[0] == "S":
        print(subtract(tokens[1], tokens[2]))
    if tokens[0] == "M":
        print(multiply(tokens[1], tokens[2]))
    if tokens[0] == "D":
        print(divide(tokens[1], tokens[2]))
    if tokens[0] == "SQ":
        print(square(tokens[1]))
    if tokens[0] == "C":
        print(cube(tokens[1]))
    if tokens[0] == "R":
        print(mod(tokens[1], tokens[2]))
    if tokens[0] == "SR":
        print(square_root(tokens[1]))
    if tokens[0] == "P":
        print(power(tokens[1], tokens[2]))


def run_calculator():
    """Main loop of functions"""
    i = True
    while i is True:
        tokens = get_input()
        check_input(tokens)
        tokens = convert_to_floats(tokens)
        call_arithmetic(tokens)
        if tokens[0].lower() == "q":
            print("You think you can calculate on your own?!!")
            sure = input("Press 'q' to quit or 'r' to restart.\n: ")
            if sure == "r":
                i = True
            else:
                i = False


run_calculator()

# when q is entered into get_input, error results if don't also enter numbers.
