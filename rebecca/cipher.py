import random


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


def decrypt(message, text, shift):
    """Decrypt the encrypted message and return it as plain text."""
    plain_text = str()
    indexes = [
        i.replace(",", "").replace("[", "").replace("]", "") for i in message.split()
    ]  # Just a precaution that the user might copy the encrypted message from the output including the brackets and commas
    for i in indexes:
        plain_text += text[int(i) - shift]
    return plain_text
