import random


while True:
    user_input = ''
    while not user_input.isdigit():
        user_input = int(input("Cliquer sur un bouton "))

    if user_input == 0:
        print("Bye, à la prochaine")
        break
    elif user_input == 1:
        print(random.randint(1, 6))
    else:
        print("Je n'ai pas compris")