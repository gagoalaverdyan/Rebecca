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
        print_encryption_message(cipher_text, text, shift)
    elif choice == "decrypt":
        plaintext = decrypt(message, text, shift)
        print_decryption_message(plaintext)

    final_choice = print_final_message()
    if final_choice in ("y", "Y"):
        print_one_time_pad(char_dict, text)
    else:
        sys.exit()


if __name__ == "__main__":
    main()
