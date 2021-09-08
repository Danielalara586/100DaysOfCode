# Day 17: Sorted List

def sortedList():
    print("Welcome to sorted list, you'll be asked to give 10 numbers to be sorted ascending and descending")
    ascending = []
    descending = []
    for i in range (10):
        i = int(input("Please enter a number: "))
        ascending.append(i)
        descending.append(i)
        ascending.sort()
        descending.sort(reverse = True)
    print (f"Lower to greater: {ascending}")
    print (f"Greater to lower: {descending} ")

    


def run():
    sortedList()


if __name__ == "__main__":
    run()