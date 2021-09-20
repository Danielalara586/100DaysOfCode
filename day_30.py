# Day 30: Distance between two points

import os
import math

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(coord_a: Coordinates, coord_b: Coordinates):
    distance = math.sqrt((coord_b.x - coord_a.x)**2 + (coord_b.y - coord_a.y)**2)
    return round(distance, 2)


def run():
    os.system("clear")
    print("Welcome to Distance Between to Points Calculator!")
    x_1 = int(input("Please enter x1 value: "))
    y_1 = int(input("Please enter y1 value: "))
    x_2 = int(input("Please enter x2 value: "))
    y_2 = int(input("Please enter y2 value: "))

    coord_a = Coordinates(x_1, y_1)
    coord_b = Coordinates(x_2, y_2)

    print(f"Distance = {distance(coord_a, coord_b)}cm")

if __name__ == "__main__":
    run()
