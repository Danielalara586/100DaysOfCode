# Day 24: Sorting names

import csv
import time
import os

def elapsed_time(function):
    def elapsed_time(*args, **kwargs):
        start = time.time()
        func = function(*args, **kwargs)
        print(f"Execution time: {time.time() - start}")
        return func
    return elapsed_time

def save_data():
    data = []
    with open("random_names.csv", 'r') as file:
        csv_reader = csv.reader(file)
    
        for name in csv_reader:
            data.append(name[0])
    
        return data
    

@elapsed_time
def bubble_sort(data):
    os.system("clear")
    print("---BUBBLE SORT---\n")
    
    sorted_data = []
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j] 

        sorted_data.append(data[i])

    print(f"Sorted data: {sorted_data} \n")

@elapsed_time
def selection_sort(data):
    print("\n---SELECTION SORT---\n")
    
    sorted_data = []
    n = len(data)

    for i in range(n):
        index = i
        for j in range(i+1, n):
            if data[index] > data[j]:
                index = j
        
        data[i], data[index] = data[index], data[i]
        sorted_data.append(data[i])

    print(f"Sorted data: {sorted_data} \n")

def run():
    data = save_data()
    bubble_sort(data)
    selection_sort(data)


if __name__ == "__main__":
    run()

