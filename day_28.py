# Day 28: Coding a Character!

import os

class Character:
    def __init__(self, name, att_points, def_points, health):
        self.name = name
        self.att_points = att_points # Attack points
        self.def_points = def_points # Defense points
        self.health = health
    
    def show_health(self):
        print(f"{self.name}'s health level: {self.health}")

    def attack(self):
        return self.name + " is attacking!"
    
    def defense(self):
        return self.name + " is defending!"

snake_man = Character("Snake Man", 4, 3, 10)
sword_master = Character("Sword Master", 5, 3, 8)

def battle(character_1: Character, character_2: Character):
    os.system("clear")
    while character_1.health > 0 and character_2.health > 0:
        print(f"Is {character_1.name}'s turn! \nStatus \n{character_1.attack()} \t{character_2.defense()}")
        character_2.health = (character_2.health + character_2.def_points) - character_1.att_points
        character_2.show_health() 
        print(f"Is {character_2.name}'s turn! \nStatus \n{character_2.attack()} \t{character_1.defense()}")
        character_1.health = (character_1.health + character_1.def_points) - character_2.att_points
        character_1.show_health()
    
    if character_1.health > 0:
        print(f"{character_1.name} wins the battle!")
    else:
        print(f"{character_2.name} wins the battle!")

if __name__ == "__main__":
    battle(snake_man, sword_master)
