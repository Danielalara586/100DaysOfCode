# Day 20: Memory Game! Part 3

import random
import os

def memory_game():
    answer = []
    player_answer = []
    char = "#$%()/&"
    for i in range(4):
        random_char = ''.join(random.choice(char)) 
        print(f"Char {i+1}: {random_char}")
        os.system("sleep 3s")
        os.system("clear")
        answer.append(random_char)

    for i in range(4):
        player = input(f"Ok, enter the correct order. \nEnter char {i+1}: ")
        os.system("clear")
        player_answer.append(player)

    print(f"System: {answer} \nPlayer: {player_answer}")


def run():
    memory_game()


if __name__ == "__main__":
    run()
