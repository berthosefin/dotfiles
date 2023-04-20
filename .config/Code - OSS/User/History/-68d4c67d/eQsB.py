import random


ASCII_LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGITS = '0123456789'
PUNCTUATION = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
long_pass = ''
char = ASCII_LETTERS + DIGITS + PUNCTUATION

while not long_pass.isdigit():
    pass_long = input("Donner la longueur du mot de passe: ")

print(random.sample(char, int(long_pass)))
