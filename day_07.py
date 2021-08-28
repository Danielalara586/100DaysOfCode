# Day 7: Rock, Paper, Scissors

import random

def menu():
    answer = input("Welcome to Rock, Paper, Scissors Game!\n"
    + "Do you know the rules? [y/n]: ")
    while True:
        if answer.lower() == 'y':
            option = int(input("Great, you're ready to start!\n"
            + "Which option would you like to try?\n"
            + "1. Single game \n2. 2/3 to win\n"))
            while True:
                if option == 1:
                    return single_game()
                elif option == 2:
                    return multi_game()
                else:
                    option = int(input("Please enter a valid option: "))
        elif answer.lower() == 'n':
            print('''Okay, This are the rules:
            1.- You need to choose one of this options: Rock, Paper o Scissors.
            2.- Rock wins against scissors, paper wins against rock and scissors win against paper.
            3.- "Single game" mode. The first one to beat the other wins.
            4.- "2/3 to win" mode. The first one to beat 2 out of 3 games wins.''')
            option = int(input("Now you're ready to start!\n"
            + "Which option would you like to try?\n"
            + "1. Single game \n2. 2/3 to win\n"))
            while True:
                if option == 1:
                    return single_game()
                elif option == 2:
                    return multi_game()
                else:
                    option = int(input("Please enter a valid option: "))
        else:
            answer = input("Please enter a valid option: ")

def single_game():
    print("Single game!")
    player = int(input("Rock[1], Paper[2], Scissors[3]?: "))
    while True:
        machine = random.randint(1,3)
        if player == machine:
               print("It's a tie!")
               player = int(input("Rock[1], Paper[2], Scissors[3]?: "))
        elif (player == 1 and machine == 2) or (player == 2 and machine == 3) or (player == 3 and machine == 1):
            print(f"Machine: {machine} \nMachine wins!")
            option = input("Want to play again? [y/n]: ")
            while True:
                if option.lower() == 'y':
                    return single_game()
                elif option.lower() == 'n':
                    print("See you soon!")
                    return
                else:
                    option = int(input("Please enter a valid option: "))

        elif (player == 1 and machine == 3) or (player == 2 and machine == 1) or (player == 3 and machine == 2):
            print(f"Machine: {machine} \nYou win!")
            option = input('Want to play again? [y/n]: ')
            while True:
                if option.lower() == 'y':
                    return single_game()
                elif option.lower() == 'n':
                    print("See you soon!")
                    return
                else:
                    option = int(input("Please enter a valid option: "))
        else:
            player = int(input("Please enter a valid option: "))

def multi_game():
    print("Multi game!")
    player = int(input('Rock [1], Paper [2] or Scissors [3]?: '))
    counter_p = 0
    counter_m = 0
    while True:
        machine = random.randint(1,3)
        if player == machine:
           print("It's a tie!")
           player = int(input("Rock[1], Paper[2], Scissors[3]?: "))
        elif (player == 1 and machine == 2) or (player == 2 and machine == 3) or (player == 3 and machine == 1):
            print(f"Machine: {machine} \nMachine's point!")
            counter_m += 1
            if counter_m == 2:
               return winner(counter_p, counter_m)
            player = int(input('Rock [1], Paper [2] or Scissors [3]?: '))
        elif (player == 1 and machine == 3) or (player == 2 and machine == 1) or (player == 3 and machine == 2):
            print(f"Machine: {machine} \nPlayer's point!")
            counter_p += 1
            if counter_p == 2:
               return winner(counter_p, counter_m)
            player = int(input('Rock [1], Paper [2] or Scissors [3]?: '))
        else:
            player = int(input("Please enter a valid option: "))

def winner(counter_p, counter_m):
    if counter_p > counter_m:
        print(f"You win!\n Machine: {counter_m} \tPlayer: {counter_p}")
        option = input("Want to play again? [y/n]: ")
        while True:
            if option.lower() == 'y':
                return multi_game()
            elif option.lower() == 'n':
                print("See you soon!")
                break
            else:
                option = int(input("Please enter a valid option: "))
    elif counter_m > counter_p: 
        print(f"Machine won!\n Machine: {counter_m} \tPlayer: {counter_p}")
        option = input("Want to play again? [y/n]: ")
        while True:
            if option.lower() == 'y':
                return multi_game()
            elif option.lower() == 'n':
                print("See you soon!")
                break
            else:
                option = int(input("Please enter a valid option: "))
    
def run():
    menu()

if __name__ == "__main__":
    run()