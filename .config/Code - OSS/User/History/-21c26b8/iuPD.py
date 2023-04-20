import random


while True:
    user_input = ''
    while not user_input.isdigit():
        user_input = int(input("Cliquer sur un bouton "))

    if user_input == 0:
        print("Bye, à la prochaine")
        break
    else:
        print(random.randint(1, 6))