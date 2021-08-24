# Day 2: Triangle's Area

import math

def triangle_area(side1, side2, side3):
    s = (side1 + side2 + side3)/2
    a = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    a = round(a,4)

    if side1 == side2 and side2 == side3:
        print(f"Equilateral triangle area: {a}")
    elif side1 != side2 and side2 != side3:
        print(f"Scalene triangle area: {a}")
    else:
        print(f"Isosceles triangle area: {a}")

def run():
    side1 = int(input("Please enter side 1: "))
    side2 = int(input("Please enter side 2: "))
    side3 = int(input("Please enter side 3: "))

    triangle_area(side1, side2, side3)


if __name__ == "__main__":
    run()

