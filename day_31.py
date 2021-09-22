# Day 31: Reverse Words!

def reverse_words(text: str):
    return ' '.join(word[::-1] for word in text.split(' '))

def run():
    text = input("Welcome to Reverse Words! \nPlease enter any words to be reversed: ")
    print(f"Revesed words: {reverse_words(text)}")


if __name__ == "__main__":
    run()

    