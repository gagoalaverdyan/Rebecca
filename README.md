# Rebecca

Rebecca is a Python application inspired by the espionage novel, 'The Key to Rebecca.' In this program, a cryptographic technique reminiscent of the one-time pad, as employed by a Nazi spy in the novel, is implemented for secure communication. The user has the flexibility to utilize any text-formatted book as a cipher for encrypting or decrypting messages. To enhance the encryption process,
users can input a shift parameter, to simulate the current-day technique used in the book.

The program uses [termcolor](https://pypi.org/project/termcolor/) package from pip for colorful output.

![image](https://i.imgur.com/Ir2ym05.png)

## Installation

```bash
mkdir rebecca
cd rebecca
git clone https://github.com/gagoalaverdyan/Rebecca.git .
pip install termcolor
```

## Usage

Make sure a .txt book is in the program's root directory to be used a sthe cifer.
```python
python ./rebecca.py
```

## Contributing

Pull requests are very welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

The program is licensed under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) and is free to download, use or distribute.