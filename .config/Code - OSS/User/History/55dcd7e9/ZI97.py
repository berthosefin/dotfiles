from random import randint


number_to_find = randint(0, 100)
remaining_attempts = 5

print("*** Le jeu du nombre mystère ***")

# Boucle principale
while remaining_attempts > 0:
    print(f"Il te reste {remaining_attempts} essai{'s' if remaining_attempts > 1 else ''}")

    # Saisie de l'utilisateur
    user_choice = input("Devine le nombre : ")
    if not user_choice.isdigit():
        print("Veuillez entrer un nombre valide.")
        continue

    user_choice = int(user_choice)

    if number_to_find > user_choice: # Plus grand
        print(f"")
    
    remaining_attempts -= 1

# Gagné ou perdu
if remaining_attempts == 0:
    pass

print("Fin du jeu.")