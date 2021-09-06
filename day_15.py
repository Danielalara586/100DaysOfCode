# Day 15: Volume calculator

# Program that calculates the volume of a cylinder, cube and sphere.
import math
import fractions

def menu():
    while True:
        option = int(input("Welcome, what would you like to calculate?\n"
        + "[1] Cylinder's Volume \n[2] Cube's Volume \n[3] Sphere's Volume\n"))
        
        if option == 1:
            height = float(input('Please enter a height value: '))
            radius = float(input('Please enter a radius value: '))
            return cylinder_volume(height, radius)
        elif option == 2:
            side = float(input('Please enter a side value: '))
            return cube_volume(side)
        elif option == 3:
            radius = float(input('Please enter a radius value: '))
            return sphere_volume(radius)
        else:
            option = int(input("Please enter a valid option: "))

def cylinder_volume(h, r):
    result = round(math.pi * (r**2) * h, 2)
    print(f"Cylinder's volume: {result} m^3")

def cube_volume(s):
    result = round(s**3, 2)
    print(f"Cube's volume: {result} m^3")

def sphere_volume(r):
    result = round(fractions.Fraction(4,3) * math.pi * (r**3), 2)
    print(f"Sphere's volume: {result} m^3")

def run():
    menu()

if __name__ == "__main__":
    run()
