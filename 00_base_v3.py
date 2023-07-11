"""
Base Component for Caesar Cipher Solver
v0 - skeleton setup
v1 - added component one
v2 - added component two
v3 - added component three

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
            long_line = ":" * 22
            print("\n", long_line)
            print("To Encrypt, enter (a).\nTo Decrypt, enter (b).")
            print(long_line, "\n")
            return response

        # if user enters 'no', program continues
        elif user_response == "no" or user_response == "n":
            response = "no"
            return response

        # if user enters invalid answer, print error message
        else:
            print("Please enter 'Yes' or 'No'")


# Creating a decorative border for the 'Welcome' statement
def decorative_statements(statement, decoration):
    sides = decoration * 2
    welcome_statement = "{} {} {}".format(sides, statement, sides)
    border = decoration * len(welcome_statement)
    print(border)
    print(welcome_statement)
    print(border)

    return ""


# Creating an Instructions functions for users that haven't used this solver before
def instructions():
    short_line = "~" * 7
    long_line = ":" * 70
    print("\n", long_line)
    print(short_line, "Caesar Cipher Solver Instructions:", short_line)
    print("This solver allows you to Encrypt (code) and Decrypt (decode) a message.\nTo Encrypt, enter (a). To Decrypt, enter (b).")
    print(long_line, "\n")


# Creating an Encryption function to encrypt a user's message
def encryption():
    # Creating character range
    first_char = ord("A")
    last_char = ord("Z")
    char_range = last_char - first_char + 1
    # Create decorative line variables
    line_one = ":" * 50
    line_two = "-" * 50
    print(line_one)
    # Ask users to enter a message to encrypt
    message = input("Enter a Message to Encrypt: ").lower()
    shift = 3
    result = ""
    # Go through the characters in the message
    for char in message.upper():
        if char.isalpha():
            decrypt_code = ord(char)
            encrypt_code = decrypt_code + shift
            if encrypt_code > last_char:
                encrypt_code -= char_range

            if encrypt_code < first_char:
                encrypt_code += char_range
            new_char = chr(encrypt_code)
            result = result + new_char
        else:
            result = result + char
    response = line_two + "\nEncrypted Message: " + result + "\n" + line_one
    return response


# Main Routine -----------------------------------------------------------------------------------------
welcome_message = "Welcome to the Caesar Cipher solver!"
decorative_line = "."
decorative_statements(welcome_message, decorative_line)

initial_question = yes_no_checker("Have you used this solver before? ")

if initial_question == "no":
    instructions()

print(encryption())
