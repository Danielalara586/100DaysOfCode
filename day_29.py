# Day 29: IP Generator

import random
import os

def ip_generator():
    ip = ''
    for i in range(4):
        random_num = random.randint(0,255)

        ip += str(random_num) + '.'
    print(f"IP Generated: {ip[:-1]}")

def run():
    os.system("clear")
    num = int(input("Welcome to IP Generator! \nHow many would you like to generate?: "))
    for i in range(num):
        ip_generator()

if __name__ == "__main__":
    run()