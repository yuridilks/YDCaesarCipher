"""
Component Two: Instructions
v1 - trialling this component

Author - Yuri Dilks
CC YD 2023
"""


# Functions  -------------------------------------------------------------------------------------------
# Checking user's answer to the program's question through Yes/No Checker function
def yes_no_checker(question):
    valid = False
    while not valid:
        user_response = input(question).lower()

        # if user enters 'yes', program continues
        if user_response == "yes" or user_response == "y":
            response = "yes"
            return response

        # if user enters 'no', program continues
        elif user_response == "no" or user_response == "n":
            response = "no"
            return response

        # if user enters invalid answer, print error message
        else:
            print("Please enter 'Yes' or 'No'")


# Creating an Instructions functions for users that haven't used this solver before
def instructions():
    print("How to use the Caesar Cipher solver")
    print("To begin, you can choose to Encrypt a message or Decrypt a message. Encrypting means to code, "
          "and Decrypting means to decode. If you want to Encrypt, press 'a'. If you want to Decrypt, press 'b'")


# Creating a decorative border for the 'Welcome' statement
def decorative_statements(statement, decoration):
    sides = decoration * 2
    welcome_statement = "{} {} {}".format(sides, statement, sides)
    border = decoration * len(welcome_statement)
    print(border)
    print(welcome_statement)
    print(border)

    return ""


# Main Routine -----------------------------------------------------------------------------------------
welcome_message = "Welcome to the Caesar Cipher solver!"
decorative_line = "."
decorative_statements(welcome_message, decorative_line)

# Calling the Instruction function
initial_question = yes_no_checker("Have you used this solver before? ")
if initial_question == "no":
    instructions()

print("Program Continues")
