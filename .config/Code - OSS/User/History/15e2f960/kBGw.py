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
            new_meal = input("Entre le nom du nouveau play: ")
            file.write(new_meal + "\n")
            file.close()
    else:
        print("Fichier 'meals.txt' introuvable !!!")

if __name__ == '__main__':
    print("""
    MENU:
    1 - Ajouter un nouveau plat
    2 - Choisir un plat au hasard
    """)
    choice = input("Entrer un nombre (1-2) : ")
    if choice == str(1):
        add_meal()
    elif choice == str(2):
        random_meal()
    else:
        choice = input("Entrer un nombre (1-2) : ")