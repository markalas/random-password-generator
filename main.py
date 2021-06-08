import random  
import os
import sys
import string

# Create a password generator that contain a minimum of 2 letters and 3 special characters

# User inputs length of desired password
# If input is less than 5 characters, 'invalid input', allow user to re-enter input
# Store randomly generated password into a list and output to .csv
# User input for file directory

# User input

rand_pass = []

def password_length_input(): # have user enter n length password
    while True:

        print('Please enter desired password length.')
        userInput = input('Length of password: ')
        len_pass = [] 

        try: # try userInput as int 
            val = int(userInput)
            if val < 5 or val > 14:
                print('Error: Length of password must between 5-14 characters.')
                continue
            elif val >= 5:
                len_pass = val
                break
        except ValueError: # if userInput is str
            print("Error: userInput String")
            continue
    
    return len_pass

len_pass = password_length_input()
print(len_pass)

def generate_password():
    string_specials = '!@%/()=?+.-'
    string_pool = string_specials + string.ascii_letters + string.digits
    pw_length = len_pass
    
    pw = ''.join(random.choice(string_pool + string_specials) for i in range(pw_length))

    return pw

password = generate_password()
print(password)

