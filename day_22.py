# Day 22: How much money can I save?

import os

def save_money(amount: float, months: int) -> float:
    INTEREST_RATE: float = 0.04
    saving: float = amount
    for i in range (months):
        saving = saving + (saving * (INTEREST_RATE))
    
    return saving

def run():
    os.system("clear")
    print("Welcome to savings calculator! \nWanna know how much money you'll save with a 4% interest rate?")
    amount = float(input("Please enter the amount: "))
    months = int(input("Please enter the months: "))
    total = round(save_money(amount, months), 2)
    print(f"You'll save ${total}!")


if __name__ == "__main__":
    run()