import random
import sys

from .rebecca.mainfunctions import *


def main():
    print("Welcome to Rebecca")  # Add short intro afetr and add colors
    choice = input("Enter 'e' to encrypt or 'd' to decrypt:\n")  # need to add checks
    message = input("Enter the message:\n")  # need to add checks
    shift = input("Enter the shift value (1-366):\n")  # need to add checks
    crypt_file = input("Enter the filename with extension (e.g. crypto.txt):\n")

    text = load_file(crypt_file)
    char_dict = make_dict(text, shift)

    if choice == "encrypt":
        cipher_text = encrypt(message, char_dict)
        if check_fails(cipher_text):
            print("\nUnique keys finding error :(")
            print("\nTry changing the provided crypt file.")
            sys.exit()  # Make a function

        print("{: >10}{: >10}{: >10}".format("Character", "Unicode", "Count"))
        for key in sorted(char_dict.keys()):
            print(
                "{: >10}{: >10}{: >10}".format(
                    repr(key()[1:-1]),
                    str(ord(key)),
                    len(char_dict[key]),
                )
            )

        print(f"\nNumber of distinct characters: {len(char_dict)}")
        print(f"Total number of characters: {len(text)}\n")
        print(f"Encrypted ciphertext = \n{cipher_text}\n")
        print(f"Decrypted plaintext = ")
        for i in cipher_text:
            print(text[i - shift], end="", flush=True)

    elif choice == "decrypt":
        plaintext = decrypt(message, text, shift)
        print(f"\nDecrypted plaintext = {plaintext}")
