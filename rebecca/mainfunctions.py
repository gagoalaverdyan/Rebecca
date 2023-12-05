import os
from collections import Counter, defaultdict


def load_file(filename):
    """Read the given file and return it as a string of lowercase characters."""
    while not filename or filename[-4:] != "txt" or not os.path.exists(filename):
        filename = input("Enter a valid .txt file name:\n")
    with open(filename, encoding="utf-8", errors="ignore") as file:
        file_string = file.read().lower()
    return file_string


def make_dict(text, shift):
    """Return a dictionary of characters and shifted indexes."""
    char_dict = defaultdict(list)
    for index, char in enumerate(text):
        char_dict[char].append(index + shift)
    return char_dict
