# Day 4: Repeat the word

def repeat_word(n: int, word: str):
    if n > 0:
        print(word)
        repeat_word(n-1, word)

def run():
    word = input("Which word would you like to repeat?: ")
    n = int(input("How many times?: "))
    repeat_word(n, word)

if __name__ == "__main__":
    run()

    