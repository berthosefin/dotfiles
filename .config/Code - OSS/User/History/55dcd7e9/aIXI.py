from random import randint

number_to_find = 70
remaining_attempts = 5

print("*** Le jeu du nombre mystère ***")

# Boucle principale
while remaining_attempts > 0:
    print(f"Il te reste {remaining_attempts} essai{'s' if remaining_attempts > 1 else ''}")

    # Saisie de l'utilisateur
    user_input = input("Devine le nombre : ")
    if not user_input.isdigit():
        print("Veuillez entrer un nombre valide.")
        continue

    user_input = int(user_input)

    if number_to_find > user_input: # Plus grand
        print(f"Le nombre mystère est plus grand que {user_input}")
    elif number_to_find < user_input: # Plus petit
        print(f"Le nombre mystère est plus petit que {user_input}")
    else: # Egal (succès)
        break
 
    remaining_attempts -= 1

# Gagné ou perdu
if remaining_attempts == 0:
    print(f"Dommage ! Le nombre mystère était {number_to_find}")
else:
    print(f"Bravo ! Le nom mystère était bien {user_input} !")
    print(f"Tu as trouvé le nombre en {6 - remaining_attempts} essai{'s' if remaining_attempts < 5 else ''}")

print("Fin du jeu.")