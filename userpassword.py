# Password Cracker

import itertools
import string

def password_cracker(username_or_email, password_length):
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    for password in itertools.product(characters, repeat=password_length):
        attempt = ''.join(password)
        print(f'Trying password: {attempt}')
        # Here you would check if the attempt matches the actual password
        # if attempt == actual_password:
        #     print(f'Password for {username_or_email} is: {attempt}')
        #     break

username_or_email = input("Enter username or email: ")
password_length = int(input("Enter password length to crack: "))
password_cracker(username_or_email, password_length)
