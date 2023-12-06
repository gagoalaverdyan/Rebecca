import random

from termcolor import *


def encrypt(message, char_dict):
    """Return a list of indexes for the caracters in the message."""
    encrypted = []
    for char in message.lower():
        char_len = len(char_dict[char])
        if char_len > 1:
            index = random.choice(char_dict[char])
        elif char_len == 1:
            index = char_dict[char][0]
        else:
            print(colored("\nCharacter {char} is not in dictionary.", "red"))
            continue
        encrypted.append(index)
    return encrypted


def decrypt(message, text, shift):
    """Decrypt the encrypted message and return it as plain text."""
    plain_text = str()
    indexes = [i for i in message.split()]
    for i in indexes:
        plain_text += text[int(i) - shift]
    return plain_text


def print_encryption_message(cipher_text, text, shift):
    print(colored("\nEncrypted message:", "yellow"))
    if len(cipher_text) > 8:
        for i in range(0, len(cipher_text), 8):
            print(" ".join(str(element).ljust(8) for element in cipher_text[i : i + 8]))
    print(colored("Decrypted message:", "red"))
    for i in cipher_text:
        print(text[i - shift], end="", flush=True)
    print()


def print_decryption_message(plaintext):
    print(colored("\nDecrypted message:", "red"))
    print(plaintext)


def print_one_time_pad(char_dict, text):
    print()
    print("{: >10}{: >10}{: >10}".format("Character", "Unicode", "Count"))
    for key in sorted(char_dict.keys()):
        print(
            "{: >10}{: >10}{: >10}".format(
                repr(key)[1:-1],
                str(ord(key)),
                len(char_dict[key]),
            )
        )
    print(colored("\nNumber of distinct characters:", "yellow"), len(char_dict))
    print(colored("Total number of characters:", "yellow"), (len(text)))


if __name__ == "__main__":
    print("Please run rebecca.py")
