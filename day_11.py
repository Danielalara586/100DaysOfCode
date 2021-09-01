# Day 11: Password Generator 

import string
import random

def password_generator(lenght: int):
    char = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(char) for i in range(lenght))

def run():
    lenghth = int(input("Please enter the lenght you want for your password: "))
    password = password_generator(lenghth)
    print(f"Your new password is: {password}")

if __name__ == "__main__":
    run()

    