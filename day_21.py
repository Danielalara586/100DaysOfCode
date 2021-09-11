# Day 21: Memory Game! Part 4 (Final Part)

import random
import os

answer = []
player_answer = []
char = "#$%()/&"
num_char = 4

def levels(option):
    os.system("clear")
    if option == 1:
        print(f"Level 1 \nCharacters appearing: {num_char}")
        os.system("sleep 3s")
        for i in range(num_char):
            random_char = ''.join(random.choice(char)) 
            print(f"Char {i+1}: {random_char}")
            os.system("sleep 3s")
            os.system("clear")
            answer.append(random_char)

        for i in range(num_char):
            player = input(f"Ok, enter the correct order. \nEnter char {i+1}: ")
            os.system("clear")
            player_answer.append(player)

    elif option == 2:
        print(f"Level 2 \nCharacters appearing: {num_char + 2}")
        os.system("sleep 3s")
        for i in range(num_char + 2):
            random_char = ''.join(random.choice(char)) 
            print(f"Char {i+1}: {random_char}")
            os.system("sleep 3s")
            os.system("clear")
            answer.append(random_char)
        
        for i in range(num_char + 2):
            player = input(f"Ok, enter the correct order. \nEnter char {i+1}: ")
            os.system("clear")
            player_answer.append(player)

    elif option == 3:
        print(f"Level 3 \nCharacters appearing: {num_char + 4}") 
        os.system("sleep 3s")  
        for i in range(num_char + 4):
            random_char = ''.join(random.choice(char)) 
            print(f"Char {i+1}: {random_char}")
            os.system("sleep 3s")
            os.system("clear")
            answer.append(random_char)

        for i in range(num_char + 4):
            player = input(f"Ok, enter the correct order. \nEnter char {i+1}: ")
            os.system("clear")
            player_answer.append(player)
    else:
        print("Please enter a valid option.")
        return memory_game() 
    
    return player_answer == answer

def play_again(answer):
    if answer.lower() == 'y':
        return memory_game()
    elif answer.lower() == 'n':
        print("Ok, see you soon!")
        return
    else:
        answer = input("Please enter a valid option: ")
        play_again(answer)

def memory_game():
    print("Welcome to memory game! \nYou'll see different characters on screen and you'll need to rembember the order.")
    option = int(input("Choose your level: \n[1] Level 1 \n[2] Level 2 \n[3] Level 3 \nOption: "))
    validation = levels(option)

    if validation:
        again = input("You won! \nWanna play again? [y/n]: ")
        play_again(again)
    else:
        again = input(f"Sorry, you entered: {player_answer} \nThe correct order was: {answer} \nWanna play again? [y/n]: ")
        play_again(again)

    

def run():
    memory_game()


if __name__ == "__main__":
    run()
