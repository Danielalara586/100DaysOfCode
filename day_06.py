# Day 6: Calculator

def calculator(num1: int, operator: str, num2: int):
    while True:
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            return num1 / num2 

def run():
    num1 = int(input("First number: "))
    operator = input("Operator: ")
    num2 = int(input("Second number: "))
    print(calculator(num1, operator, num2))

if __name__ == "__main__":
    run()

