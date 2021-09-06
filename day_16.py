# Day 16: Calculator 2.0

def calculator_v2():
    while True:
        option = int(input('''\tWelcome to calculator 2.0, where you can add or multiply as many numbers as you want!
        Please select an option:
        [1] Add numbers
        [2] Multiply numbers
        '''))
        if option == 1:
            number = int(input("Press 0 to end the program \nPlease enter a number: "))
            total = 0
            while number != 0:
                total += number
                number = int(input("Please enter another number: "))
            return total
        elif option == 2:
            number = int(input("Press 0 to end the program \nPlease enter a number: "))
            total = 1
            while number != 0:
                total *= number
                number = int(input("Please enter another number: "))
            return total
        else:
            option = int(input("Please enter a valid opiton: "))


def run():
    result = calculator_v2()
    print(f"Result: {result}")


if __name__ == "__main__":
    run()