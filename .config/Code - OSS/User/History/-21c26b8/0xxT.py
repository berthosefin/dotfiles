import random


while True:
    user_input = input("Cliquer sur un bouton ")
    if int(user_input) == 0:
        break
    else:
        print(random.randint(1, 6))