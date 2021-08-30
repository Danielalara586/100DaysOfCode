# Day 9: Secret Number

import random

def secret_number():
    print("Welcome to Secret number!\n" +
    "You have 3 tries to guess the computer's secret number.")
    machine_num = random.randint(1,100)
    tries = 0
    while tries < 3:
        player_num = int(input("Please enter a number beetween 1 and 100: "))
        if player_num == machine_num:
            tries += 1
            print(f"You won! \nTries: {tries}")
            return play_again()
        elif player_num > machine_num and player_num < 101:
            print("Lower")
            tries += 1
        elif player_num < machine_num and player_num > 0:
            print("Higher")
            tries += 1
        else:
            print("Please enter a valid option.")
    print(f"Sorry, you lost. \nThe secret number was: {machine_num}")
    return play_again()

def play_again():
    option = input("Want to play again? [y/n]: ")
    while True:
        if option.lower() == 'y':
            return secret_number()
        elif option.lower() == 'n':
            print("See you soon!")
            return
        else:
            option = input("Please enter a valid option: ")

def run():
    secret_number()

if __name__ == "__main__":
    run()