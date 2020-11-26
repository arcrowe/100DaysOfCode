import winsound
import time
from itertools import chain


# first - create the `dot` and `line` functions
def dot():
    winsound.Beep(800, 300)
    time.sleep(0.1)  # this is in seconds


def dash():
    winsound.Beep(800, 600)
    time.sleep(0.1)


def between_letters():
    time.sleep(1)


def between_words():
    time.sleep(2)


# now you need some way of mapping letters to sounds
mapping = {
    "a": ['.', '-'],
    "b": ['-', '.', '.', '.'],
    'c': ['-', '.', '-', '.'],
    'd': ['-', '.', '.'],
    'e': '.',
    'f': ['.', '.', '-', '.'],
    'g': ['-', '-', '.'],
    'h': ['.', '.', '.', '.'],
    'i': ['.', '.'],
    'j': ['.', '-', '-', '-'],
    'k': ['-', '.', '-'],
    'l': ['.', '-', '.', '.'],
    'm': ['-', '-'],
    'n': ['-', '.'],
    'o': ['-', '-', '-'],
    'p': ['.', '-', '-', '.'],
    'q': ['-', '-', '.', '-'],
    'r': ['.', '-', '.'],
    's': ['.', '.', '.'],
    't': '-',
    'u': ['.', '.', '-'],
    'v': ['.', '.', '.', '-'],
    'w': ['.', '-', '-'],
    'x': ['-', '.', '.', '-'],
    'y': ['-', '.', '-', '-'],
    'z': ['-', '-', '.', '-'],
    ' ': ' ',
    '1': ['.', '-', '-', '-', '-'],
    '2': ['.', '.', '-', '-', '-'],
    '3': ['.', '.', '.', '-', '-'],
    '4': ['.', '.', '.', '.', '-'],
    '5': ['.', '.', '.', '.', '.'],
    '6': ['-', '.', '.', '.', '.'],
    '7': ['-', '-', '.', '.', '.'],
    '8': ['-', '-', '-', '.', '.'],
    '9': ['-', '-', '-', '-', '.'],
    '0': ['-', '-', '-', '-', '-'],

}


# translate into sounds
def play_morse(message) -> object:
    for letter in message:
        if letter[0] != '':
            for char in letter:
                if char != ' ':
                    if char == '.':
                        dot()
                    elif char == '-':
                        dash()
            between_letters()
        else:
            between_words()


def get_user_word():
    word1 = input('Enter word (only letters, spaces and digits): ')

    if all([True if c in mapping else False for c in word1]):
        return word1.lower()
    else:
        print('non alphanumeric characters - try again')


word = ''
morse = []
while not word:
    word = get_user_word()
    if word:
        for char in word:
            add_me = "".join(mapping[char])
            morse.append(add_me)

        morseString = ''.join(chain.from_iterable(morse))
        print(morseString)
        # print(morse)
        play_morse(morse)
