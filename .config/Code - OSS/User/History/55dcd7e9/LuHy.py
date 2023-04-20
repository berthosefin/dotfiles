from random import randint


MYSTERE = randint(0, 100)
essai = 5
for i in range(5):
    print(f"Il te reste {essai} essais")
    user_input = input("Devine le nombre : ")
    while not user_input.isdigit():
        print("Veillez entrer un nombre valide.")
    essai -= 1
    if int(user_input) > MYSTERE:
        print(f"Le nombre mystère est plus petit que {user_input}")
    elif int(user_input) < MYSTERE:
        print(f"Le nombre mystère est plus grand que {user_input}")
    else:
        print(f"")
print(f"Dommage ! Le nombre mystère était {MYSTERE}")