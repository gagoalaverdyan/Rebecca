import random
import sys

from .rebecca.mainfunctions import *


def main():
    welcome_message()
    choice = make_choice()  # Add colors, q to exit
    message = enter_message()  # Add colors, q to exit
    shift = enter_shift()  # Add colors, q to exit
    crypt_file = get_cipher_file()  # Add colors, q to exit

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
