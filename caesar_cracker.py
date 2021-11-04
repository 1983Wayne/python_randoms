# Caesar Cipher Brute force function
# 3 November 2021
# Version 1.0
# NOTE: Capitals only, spaces not a part of the shift
# Wayne Caissie



def caesar_cipher():
    """This script will brute force a solution to a shift cipher."""
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'                                  # Creates legal letters
    new_message = ''                                                        # Used in the code to create an output message
    message = input('What\'s the message? >  ')                             # Input message
    key = 0
    while key <= 26:
        for i in message:
            if i == " ":                                                    # If current letter is actually a space
                new_message += i                                            # Go ahead and add just the space to the message
            elif letters.index(i) - key < 0:                                # The next few lines deal with wrapping around
                letter_index = (letters.index(i) - key) + len(letters)
            else:
                letter_index = (letters.index(i) - key)
            if i != " ":                                                    # When current letter in the message isn't a space
                new_message += letters[letter_index]                        # Add the changed letter to the new message
        print(new_message)                                                  # Display the message using the current 's' or key 
        key += 1
        new_message = ""                                                    # Increments the key or 's' value and resets the message
