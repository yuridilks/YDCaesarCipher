"""
Component One: Encrypt Solver
v1 - trialling this component
v2 - adding user input

Author - Yuri Dilks
CC YD 2023
"""


# Functions
def encryption():
    # Ask users to enter a message to encrypt
    message = input("Encryption Message: ").lower()
    shift = 3
    # Placeholder for result
    result = ""
    # Go through the characters in the message
    for char in message:
        # isalpha checks if the characters are in the alphabet or not
        if char.isalpha():
            # Change the characters in the message into the ASCII code
            decrypt_code = ord(char)
            # Creating the encrypted characters by shifting the characters
            encrypt_code = decrypt_code + shift
            new_char = chr(encrypt_code)
            # If the character is in the alphabet, encrypt it
            result = result + new_char
        else:
            # If the character is not in the alphabet, keep it the same
            result = result + char
    print(result)


# Main Routine
print(encryption())
