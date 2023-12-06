import sys

from rebecca.cipher import *
from rebecca.mainfunctions import *


def main():
    welcome_message()
    choice = make_choice()
    message = enter_message()
    crypt_file = get_cipher_file()
    shift = enter_shift()

    text = load_file(crypt_file)
    char_dict = make_dict(text, shift)

    if choice == "encrypt":
        cipher_text = encrypt(message, char_dict)
        failure_check(cipher_text)
        print_encrypted_message(char_dict, shift, cipher_text, text)

    elif choice == "decrypt":
        plaintext = decrypt(message, text, shift)
        print(f"\nDecrypted plaintext = {plaintext}")


if __name__ == "__main__":
    main()
