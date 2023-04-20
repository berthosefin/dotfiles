import random


random_number = random.randint(0, 100)
user_input = input("Saisir un nombre: ")
if int(user_input) < random_number:
