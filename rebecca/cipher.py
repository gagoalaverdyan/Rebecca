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
            print("\nCharacter {char} is not in dictionary.")
            continue
        encrypted.append(index)
    return encrypted


def print_encrypted_message(char_dict, shift, cipher_text, text):
    print("{: >10}{: >10}{: >10}".format("Character", "Unicode", "Count"))
    for key in sorted(char_dict.keys()):
        print(
            "{: >10}{: >10}{: >10}".format(
                repr(key)[1:-1],
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


def decrypt(message, text, shift):
    """Decrypt the encrypted message and return it as plain text."""
    plain_text = str()
    indexes = [
        i.replace(",", "").replace("[", "").replace("]", "") for i in message.split()
    ]  # Just a precaution that the user might copy the encrypted message from the output including the brackets and commas
    for i in indexes:
        plain_text += text[int(i) - shift]
    return plain_text


if __name__ == "__main__":
    print("Please run rebecca.py")
