import os
import sys
from collections import Counter, defaultdict

from termcolor import *

# Basic things are implemented as functions to avoid errors from the user's side and to make the code more readable.


def welcome_message():
    """Print a welcome message for the program."""
    print(
        " ______________________________________________________________________",
        "|                                                                      |",
        sep="\n",
    )
    print(
        "|                            ",
        colored("WELCOME TO REBECCA", "green"),
        "                        |",
        end="\n",
        sep="",
    )
    print(
        "|______________________________________________________________________|",
        "|                                                                      |",
        "| Rebecca is a powerful message encryption/decryption program.         |",
        "| Inspired by the novel 'The Key to Rebecca', it requres a .txt book   |",
        "| as the cipher. So make sure the file is in the program's directory.  |",
        "| It also requires a shift value for better encryption of the message. |",
        "|______________________________________________________________________|",
        sep="\n",
    )


def make_choice():
    """Receive user's intention to encrypt or decrypt the message and return it."""
    print(colored("\n  1. Enter 'e' to encrypt a message", "yellow"))
    print(colored("  2. Enter 'd' to decrypt a message", "yellow"))
    print(colored("  3. Enter 'q' to to quit the program", "yellow"))

    while True:
        choice = input()
        if choice not in ("d", "D", "e", "E", "q", "Q"):
            print(colored("Wrong option. Please re-enter:", "red"))
        if choice in ("e", "E"):
            return "encrypt"
        elif choice in ("d", "D"):
            return "decrypt"
        elif choice in ("q", "q"):
            sys.exit()


def enter_message():
    """Receive user's message to encrypt or decrypt and return it."""
    while True:
        message = str(input(colored("\nEnter the message or 'q' to quit:\n", "green")))
        if not message:
            print(colored("No input received.", "red"))
        if message in ("q", "Q"):
            sys.exit()
        else:
            return message


def get_cipher_file():
    """Receive the name of the file to be used as the cipher and return it."""
    while True:
        filename = str(
            input(
                colored(
                    "Enter the cipher filename with extension (e.g. crypto.txt) or 'q' to quit:\n",
                    "green",
                )
            )
        )
        if not filename or filename[-4:] != ".txt" or not os.path.exists(filename):
            print(colored("File entered is not a .txt or does not exist.", "red"))
        elif filename in ("q", "Q"):
            sys.exit()
        else:
            return filename


def enter_shift():
    """Receive a number in the range 1-365 to simulate the daily shift and encrypt or decrypt characters."""
    while True:
        shift = input(
            colored("Enter the shift value (1-365) or 'q' to quit:\n", "green")
        )
        try:
            if shift in ("q", "Q"):
                sys.exit()
            else:
                shift = int(shift)
                if 1 <= shift <= 365:
                    return shift
                else:
                    print(colored("The shift value must be in the range 1-365.", "red"))
        except ValueError:
            print(colored("Please enter a valid integer in the range 1-365.", "red"))


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


def failure_check(cipher):
    """Check whether cipher text containing duplicate keys."""
    check = [k for k, v in Counter(cipher).items() if v > 1]
    if len(check) > 0:
        print(colored("\nUnique keys finding error :(", "red"))
        print(colored("Try changing the provided crypt file.", "red"))
        sys.exit()


def print_final_message():
    print(colored("\nShow the one-time pad generated based on the cipher?", "green"))
    print(colored("Enter 'y' for Yes or 'n' for No", "green"))
    final_choice = input()
    return final_choice


if __name__ == "__main__":
    print("Please run rebecca.py")
