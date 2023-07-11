"""
Component Four: Decrypt Solver
v1 - trialling this component

Author - Yuri Dilks
CC YD 2023
"""
first_char = ord("A")
last_char = ord("Z")
char_range = last_char - first_char + 1


# Functions
def decryption():
    # Create decorative line variables
    decorative_line = "," * 50
    line = "-" * 50
    print(decorative_line)
    # Ask users to enter a message to encrypt
    message = input("Enter a Message to Decrypt: ").lower()
    shift = -3
    # Placeholder for result
    result = ""
    # Go through the characters in the message
    for char in message.upper():
        # isalpha checks if the characters are in the alphabet or not
        if char.isalpha():
            # Change the characters in the message into the ASCII code
            decrypt_code = ord(char)
            # Creating the encrypted characters by shifting the characters
            decrypt_code = decrypt_code + shift

            if decrypt_code > last_char:
                decrypt_code -= char_range

            if decrypt_code < first_char:
                decrypt_code += char_range

            new_char = chr(decrypt_code)
            # If the character is in the alphabet, encrypt it
            result = result + new_char
        else:
            # If the character is not in the alphabet, keep it the same
            result = result + char
    response = line + "\nDecrypted Message: " + result + "\n" + decorative_line
    return response


# Main Routine
print(decryption())
