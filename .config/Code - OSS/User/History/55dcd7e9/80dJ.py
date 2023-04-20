from random import randint


MISTERE = randint(0, 100)
essai = 5
for i in range(5):
    print(f"Il te reste {essai} essais")
    user_input = input("Devine le nombre : ")
    while not user_input.isdigit():
        print("Veillez entrer un nombre valide.")
    if int(user_input) > MISTERE:
        print(f"Le nombre mystère est plus petit que {user_input}")

    