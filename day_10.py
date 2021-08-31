# Day 10: Pig Latin Translator 

def translator(word: str):
    vowels = "aeiou"
    consonants = "bcdfghijklmnpqrstvwxyz"

    while True:
        if word[0].lower() in vowels:
            return (word+"way").lower()
        elif word[0].lower() in consonants:
            return (word[1:len(word)]+word[0]+"ay").lower()
        else:
            word = input("Please enter a word: ")
            

def run():
    word = input("Please enter a word: ")
    new_word = translator(word)
    print(f"The new word is: {new_word}")

if __name__ == "__main__":
    run()