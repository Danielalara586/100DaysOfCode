# Day 25: Sorting digits


def descending_order(num):
    sorted_data = []
    n = len(str(num))
    array = []
    for i in str(num):
        array.append(i)

    for i in range(n):
        index = i
        for j in range(i+1, n):
            if array[index] < array[j]:
                index = j
        
        array[i], array[index] = array[index], array[i]
        sorted_data.append(array[i])

    new_num = ''.join(sorted_data)
    return int(new_num)


def run():

    number = int(input("Welcome to sorted digits! \nYou can enter any number you want and I'll sort the digits in descending order"
    + "\nPlease enter a number (at least 2 digits long): "))
    
    print(f"Sorted digits: {descending_order(number)}")

if __name__ == "__main__":
    run()