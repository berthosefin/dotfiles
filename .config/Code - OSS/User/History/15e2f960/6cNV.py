import os

if os.path.exists("meals.txt"):
    with open("meals.txt", "rw+") as file:
        pass
else:
    print("Fichier 'meals.txt' introuvable !!!")
