import os
import random

if os.path.exists("meals.txt"):
    with open("meals.txt", "rw+") as file:
        meals_list = file.readlines()
        random_meal = random.choice(meals_list)
else:
    print("Fichier 'meals.txt' introuvable !!!")
