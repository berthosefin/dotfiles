import os
import random

if os.path.exists("meals.txt"):
    with open("meals.txt", "rw+") as file:
        meals_list = file.readlines()
else:
    print("Fichier 'meals.txt' introuvable !!!")
