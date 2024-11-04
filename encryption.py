import random
import string

#instead of writing manually, we have borrowed the symbols, alphabets and numbers from the 'string' library
encrypted_characters = " " + string.punctuation + string.digits + string.ascii_letters
en_char = list(encrypted_characters)
key = en_char.copy()

random.shuffle(key)
#print (f"characters{en_char}")
#print (f"key{key}")

#encryption
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = en_char.index(letter)
    cipher_text += key[index]

print (f"Original message: {plain_text}")
print (f"Encrypted message: {cipher_text}")