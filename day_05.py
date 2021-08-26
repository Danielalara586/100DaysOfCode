# Day 5: No vowels

def no_vowels(text: str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for vowel in vowels:
        text = text.replace(vowel, '')
    print(f"Your text without vowels is: \n {text}")

def run():
    text = input("Please enter a text: ")
    no_vowels(text)

if __name__ == "__main__":
    run()