# Day 32: Alphabetic Position

def alphabet_position(text):
    numeric_position = ''
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for i in text:
        if i.isalpha():
            numeric_position += str(alphabet.index(i.lower()) + 1) + ' '
    return numeric_position[0:len(numeric_position) - 1]


def run():
    print("Welcome to Alphabetic Position!\n" +
    "This program will show you the numeric position of each letter of a word or text.")
    text = input("Please enter a word or text: ")
    replace = alphabet_position(text)
    print(f"Numeric position: {replace}")

if __name__ == "__main__":
    run()