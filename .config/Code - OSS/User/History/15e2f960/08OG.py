import os
import random

def random_meal():
    if os.path.exists("meals.txt"):
        with open("meals.txt", "r+") as file:
            meals_list = file.readlines()
            random_meal = random.choice(meals_list)
            print(f"Je vous propose : {random_meal}")
    else:
        print("Fichier 'meals.txt' introuvable !!!")


def add_meal():
    if os.path.exists("meals.txt"):
        with open("meals.txt", "a+") as file:
            new_meal = input("Entre le nom : ")
            file.write(new_meal)
            file.close()
    else:
        print("Fichier 'meals.txt' introuvable !!!")