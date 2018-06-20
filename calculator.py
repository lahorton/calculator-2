"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
print("Welcome to our calculator")
numbers = input("Please enter your desired action, with operator first. i.e. add 2 3. \n: ")
numbers = numbers.rstrip()
tokens = numbers.split(" ")
print(tokens)

