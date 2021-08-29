# Day 8: Cylinder's Volumme

import math

def cylinder_volume(h: int, r: int) -> int:
    return math.pi * (r**2) * h

def run():
    height = int(input("Please enter the height: "))
    radius = int(input("Please enter the radius: "))
    result = round(cylinder_volume(height, radius), 2)
    print(f"The cylinder's volume is {result}m^3.")

if __name__ == "__main__":
    run()
