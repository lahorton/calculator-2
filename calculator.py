"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


print("Welcome to our calculator")


def get_input():
    """Get's initial user input and tokenizes."""
    numbers = input("Enter action, with operator first. i.e. add 2 3. \n: ")
    numbers = numbers.rstrip()
    tokens = numbers.split(" ")
    print(tokens)
    return tokens


tokens = get_input()


def check_input():
    """Checking user input for correct type and format."""
    while True:
        if tokens[0].isalpha():
            for num in tokens[1:]:
                if num.isdigit():
                    return False
                else:
                    print("Please type digits aka 1, -4, 1000.")
                    get_input()
        else:
            print("Please choose action from the menu.")
            # Print menu
            get_input()

    print("Excellent, let me think for a moment...")


check_input()
