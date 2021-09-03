# Day 13: Tip Calculator 

def tip_calculator():
    print("Enter 0 to stop counting")
    subtotal = 0
    total = 0

    while True:
        price = int(input("Food's price: $"))
        if price != 0:
            subtotal += price
        else:
            tip = int(input("Tip percentage: "))
            return round(subtotal + (subtotal * (tip / 100)), 2)

def run():
    total = tip_calculator()
    print(f"Total Bill Price: ${total}")


if __name__ == "__main__":
    run()
