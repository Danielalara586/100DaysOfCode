#Day 26: Morse Code

def morse_code(word: str):
    message = ''
    morse = {'A': ".-", 'B': "-...", 'C': "-.-.",
    'D': "-..", 'E': ".", 'F': "..-.", 'G': "--.",
    'H': "....", 'I': "..", 'J': ".---", 'K': "-.-",
    'L': ".-..", 'M': "--", 'N': "-.", 'O': "---",
    'P': ".--.", 'Q': "--.-", 'R': ".-.", 'S': "...",
    'T': "-", 'U': '..-', 'V': "...-", 'W': ".--", 
    'X': "-..-", 'Y': "-.--", 'Z': "--..", ' ': ' '}

    for letter in word:
        message += morse[letter.capitalize()] + ' '

    return message
                
    

def run():
  word = input("Welcome to Morse Code! \nPlease enter a word to be transform: ")
  print(f"Your message in Morse code: {morse_code(word)}")



if __name__ == "__main__":
  run()