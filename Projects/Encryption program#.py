#encryption programn
import random
import string

chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)

key = chars.copy()

random.shuffle(key)

org = input("Enter your message to be encrypted: ")
cipher = ""

print("Your Encrypted message will be: ", end="")

for letter in org:
    index = chars.index(letter)
    encrypted = letter.replace(letter, key[index])
    cipher += encrypted
print(cipher)


ciph = input("Enter your message to be decrypted: ")
orig = ""

print("Your decrypted message will be: ", end="")

for letter in ciph:
    index = key.index(letter)
    decrypted = letter.replace(letter, chars[index])
    ciph += decrypted
print(ciph)

