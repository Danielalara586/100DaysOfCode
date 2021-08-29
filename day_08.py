# Day 8: Cilinder's Volumme

import math

def cilinder_volume(h: int, r: int) -> int:
    return math.pi * (r**2) * h

def run():
    height = int(input("Please enter the height: "))
    radius = int(input("Please enter the radius: "))
    result = round(cilinder_volume(height, radius), 2)
    print(f"The cilinder's volume is {result}m^3.")

if __name__ == "__main__":
    run()