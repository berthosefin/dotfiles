import random


RANDOM_NUMBER = random.randint(0, 10)
ESSAI = 3

for i in range(3):
    user_input = ''
    while not user_input.isdigit():
        user_input = input("Saisir un nombre: ")

    if int(user_input) == RANDOM_NUMBER:
        print(f"Bravo! {user_input} est le bon numéro.")
        break
    elif int(user_input) > RANDOM_NUMBER:
        print("Plus pétit")
    elif int(user_input) < RANDOM_NUMBER:
        print("Plus grand")

    ESSAI -= 1
    print('-' * 50)

if ESSAI > 0:
    print(f"Vous l'avez trouvez en {ESSAI+1 - ESSAI} essai")
else:
    print("Vous avez perdu!")