import random


RANDOM_NUMBER = random.randint(0, 10)
user_input = ''
while not user_input.isdigit():
    user_input = input("Saisir un nombre: ")

if int(user_input) < random_number:
    print("Plus grand")
else:
    print("Plus petit")