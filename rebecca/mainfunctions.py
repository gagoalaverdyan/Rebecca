import os
from collections import Counter, defaultdict

# Basic things are implemented as functions to avoid errors from the user's side and to make the code more readable.


def welcome_message():
    """Print a welcome message for the program."""
    print("Welcome to Rebecca")  # Add short intro after and add colors,


def make_choice():
    """Receive user's intention to encrypt or decrypt the message and return it."""
    choice = input("Enter 'e' to encrypt or 'd' to decrypt:\n")
    while choice not in ("d", "e"):
        choice = input("Wrong option. Enter 'e' to encrypt or 'd' to decrypt:\n")
    if choice == "e":
        return "encrypt"
    else:
        return "decrypt"


def enter_message():
    """Receive user's message to encrypt or decrypt and return it."""
    message = str(input("Enter the message:\n"))
    while not message:
        message = input("No input received.\nEnter the message:\n")
    return message


def enter_shift():
    """Receive a number in the range 1-365 to simulate the daily shift and encrypt or decrypt characters."""
    shift = input("Enter the shift value (1-365):\n")
    while not shift or type(shift) != int or not 1 <= shift <= 365:
        shift = input("The shift value must be an integer in the range 1-365:\n")
    return shift


def get_cipher_file():
    """Receive the name of the file to be used as the cipher and return it."""
    filename = str(
        input("Enter the cipher filename with extension (e.g. crypto.txt):\n")
    )
    while not filename or filename[-4:] != ".txt" or not os.path.exists(filename):
        filename = input("Enter a valid .txt file name:\n")
    return filename


def load_file(filename):
    """Read the given file and return it as a string of lowercase characters."""
    with open(filename, encoding="utf-8", errors="ignore") as file:
        file_string = file.read().lower()
    return file_string


def make_dict(text, shift):
    """Return a dictionary of characters and shifted indexes."""
    char_dict = defaultdict(list)
    for index, char in enumerate(text):
        char_dict[char].append(index + shift)
    return char_dict
