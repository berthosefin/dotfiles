from random import random


# tp: Jeu du Juste Prix
# choisir un nombre entre 1 et 1000
random_n = random()

# tant que le jeu n'est pas fini
#   -> demander à l'utilisatuer "entrer un prix"
#   -> si il trouve le juste prix "c'est gagné !"
#   -> sinon on affiche "c'est moins" ou "c'est plus"
while True:
    user_input = int(input("Entrer un prix: "))
    if user_input == random_n:
        print("C'est gagné !")
        break
    elif user_input < random_n:
        print("C'est moins")
    elif user_input > random_n:
        print("C'est plus")