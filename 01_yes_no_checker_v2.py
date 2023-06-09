"""
Component One: Yes/No Checker
v1 - trialling this component
v2 -

Author - Yuri Dilks
CC YD 2023
"""


# Functions  -----------------------------------------------------------
# Checking user's answer to the program's question through Yes/No Checker function
def yes_no_checker(question):
    valid = False
    while not valid:
        user_response = input(question).lower()

        # if user enters 'yes', program continues
        if user_response == "yes" or user_response == "y":
            print("Program Continues")
            return yes_no_checker

        # if user enters 'no', program continues
        elif user_response == "no" or user_response == "n":
            print("Show Instructions, Program Continues")
            return yes_no_checker

        # if user enters invalid answer, print error message
        else:
            print("Please enter 'Yes' or 'No'")


# Main Routine ---------------------------------------------------------
initial_question = yes_no_checker("Have you used this Caesar Cipher solver before? ")
