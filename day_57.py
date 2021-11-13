# Day 57: Password finder

import hashlib

found = 0
input_hash = input("Please enter the hashed password: ")
pass_doc = input("Please enter the dictionary: ")

try:
    pass_file = open(pass_doc, "r")

except:
    print(f"Error: {pass_doc} wasn't found")

for word in pass_file:
    encrypted_word = word.encode("utf-8")
    hashed_word = hashlib.md5(encrypted_word.strip())
    digest = hashed_word.hexdigest()

    if digest == input_hash:
        print(f"The password has been found!\n The password is: {word}")
        found = 1
        break

if not found:
    print(f"The password wasn't found in the file {pass_doc}")
