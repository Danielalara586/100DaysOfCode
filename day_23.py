# Day 23: Upgrading the savings calculator

import os

os.system("clear")
print("Welcome to savings calculator! \nWanna know how much money you'll save with a 4% interest rate?")
saved_money = {}

def upgraded_calculator(amount: float, months: int):
    INTEREST_RATE: float = 0.04
    saving: float = amount
    for i in range (months):
        saving = saving + (saving * (INTEREST_RATE))

    return saving

def savings():
    x = int(input("How many amounts do you want to add?: "))
    for i in range(x):
        amount = float(input("Please enter an amount: "))
        months = int(input("Please enter the months: "))
        total = round(upgraded_calculator(amount, months), 2)
        
        saved_money[amount] = months


    return saved_money


def run():
    total = savings()
    for key in total:
        print(f"You'll save ${key} in {total[key]} months.")


if __name__ == "__main__":
    run()
