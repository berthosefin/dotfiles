import random


ASCII_LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGITS = '0123456789'
PUNCTUATION = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
pass_long = ''
char = ASCII_LETTERS + DIGITS + PUNCTUATION

while not pass_long.isdigit():
    pass_long = input("Donner la longueur du mot de passe: ")

random.sample(char, pass_long)
