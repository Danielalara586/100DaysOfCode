# Day 19: Memory Game! Part 2

import random

def memory_game():
    char = "#$%()/&"
    for i in range(4):
        random_char = ''.join(random.choice(char)) 
        print(f"Char {i+1}: {random_char}")

def run():
    print("Random Character Recording")
    memory_game()

if __name__ == "__main__":
    run()