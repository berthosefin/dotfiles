import random


ASCII_LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGITS = '0123456789'
PUNCTUATION = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
pass_long = ''
char = ASCII_LETTERS.join(DIGITS).join(PUNCTUATION)

# while not pass_long.isdigit():
#     pass_long = input("Donner la longueur du mot de passe: ")

print(char)