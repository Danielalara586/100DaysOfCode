#Day 14: All prime numbers

def prime_numbers():
    n = int(input('Please enter a number greater than 1: '))
    if n > 1:
        for i in range (2,n+1):
            num = 2
            prime = True 
            while prime and num < i:
                if i % num == 0:
                    prime = False
                else:
                    num += 1
            if prime:
                print(i)
    else:
        print('Please enter a valid number.')
        prime_numbers()
        

def run():
    prime_numbers()
    print("These are all the prime numbers.")


if __name__ == "__main__":
    run()