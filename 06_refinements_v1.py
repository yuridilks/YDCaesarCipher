"""
Component Six: Refinements
v1 - first refinement (instructions)

Author - Yuri Dilks
CC YD 2023
"""
import random


# Functions  -------------------------------------------------------------------------------------------
# Creating a decorative border for the 'Welcome' statement
def decorative_statements(statement, decoration):
    sides = decoration * 2
    welcome_statement = "{} {} {}".format(sides, statement, sides)
    border = decoration * len(welcome_statement)
    print(border)
    print(welcome_statement)
    print(border)
    return ""


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
    short_line = "~" * 7
    break_lines = "~" * 80
    long_line = ":" * 80
    print("\n", long_line)
    print(short_line, "Caesar Cipher Solver Instructions:", short_line)
    print("* If you are using the Encryption Solver, you will be given a 'key'.\n"
          " Remember this key if you wish to decrypt the same message.\n", break_lines, "\n"
          "* If you are using the Decryption Solver, \nyou can copy and paste the encrypted"
          " message from the Encrypted Solver.\n", break_lines, "\n"
          "* If your decrypted message doesn't match your original message, \nmake sure you"
          " have entered the correct key.")
    print(long_line, "\n")


# Checking if user's want to Encrypt or Decrypt a message
def encrypt_decrypt(question):
    valid = False
    while not valid:
        user_response = input(question).lower()

        # if user enters 'a', encrypt solver continues
        if user_response.lower() == "a":
            encryption()
            return user_response
        # if user enters 'b', decrypt solver continues
        elif user_response.lower() == "b":
            decryption()
            return user_response
        # if user enters 'c', program ends
        elif user_response.lower() == "c":
            return user_response

        # if user enters invalid answer, print error message
        else:
            print()


# Creating an Encryption function to encrypt a user's message
def encryption():
    # Create decorative line variables
    line_one = ":" * 50
    line_two = "-" * 50
    print(line_one)
    # Creating a character range
    first_char = ord("A")
    last_char = ord("Z")
    char_range = last_char - first_char + 1
    # Ask users to enter a message to encrypt
    message = input("Enter a Message to Encrypt: ").lower()
    shift_options = [3, 5, 7]
    shift = random.choice(shift_options)
    result = ""
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
    final_message = line_two + "\nEncrypted Message: " + result + "\n" + line_two
    print(final_message)
    print("Your Key: ", shift, "\nRemember this number if you wish to decrypt this message\n" + line_one)


def decryption():
    # Create decorative line variables
    line_one = "," * 50
    line_two = "-" * 50
    print(line_one)
    # Creating a character range
    first_char = ord("A")
    last_char = ord("Z")
    char_range = last_char - first_char + 1
    # Ask users to enter a message to encrypt
    message = input("Enter a Message to Decrypt: ").lower()
    while True:
        try:
            user_shift = int(input("Your Key: "))
            break
        except ValueError:
            print("Please enter your given 'key' from the Encryption solver (as an integer)\n", line_two)
    shift = -abs(int(user_shift))
    result = ""
    for char in message.upper():
        if char.isalpha():
            encrypt_code = ord(char)
            decrypt_code = encrypt_code + int(shift)
            if decrypt_code > last_char:
                decrypt_code -= char_range

            if decrypt_code < first_char:
                decrypt_code += char_range
            new_char = chr(decrypt_code)
            result = result + new_char
        else:
            result = result + char
    response = line_two + "\nDecrypted Message: " + result + "\n" + line_one
    print(response)


# Main Routine -----------------------------------------------------------------------------------------
welcome_message = "Welcome to the Caesar Cipher solver!"
decorative_line = "."
decorative_statements(welcome_message, decorative_line)

initial_question = yes_no_checker("Have you used this solver before? ")
if initial_question == "no":
    instructions()

user_action = encrypt_decrypt("To Encrypt, enter (a)\nTo Decrypt, enter (b)\nTo Exit, enter (c)\nYour Answer: ")
