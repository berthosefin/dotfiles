import random


print('''
1: Lancer le dé
2: Quitter le programme''')
while True:
    user_input = ''
    while not user_input.isdigit():
        user_input = input("Cliquer sur un bouton ")

    if user_input == '0':
        print("Bye, à la prochaine")
        break
    elif user_input == '1':
        print(random.randint(1, 6))
    else:
        print("Je n'ai pas compris")
    
    print('-' * 50)