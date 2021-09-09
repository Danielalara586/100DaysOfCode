# Day 18: Memory Game! Part 1

import random 

def memory_game():
    char = "#$%()/&"
    return ''.join(random.choice(char)for i in range(4)) 

def run():
    chars = memory_game()
    print(f"Random charactes: {chars}")

if __name__ == "__main__":
    run()
