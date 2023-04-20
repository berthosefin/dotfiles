import os
import random


def list_meals():
    if os.path.exists("meals.txt"):
        with open("meals.txt", "r+") as file:
            meals_list = file.readlines()
            print()
            print("LISTES DES PLATS : ")
            for meal in meals_list:
                print(meal)
    else:
        print("Fichier 'meals.txt' introuvable !!!")


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
            new_meal = input("Entre le nom du nouveau plat : ")
            file.write(new_meal + "\n")
            file.close()
        list_meals()
    else:
        print("Fichier 'meals.txt' introuvable !!!")

if __name__ == '__main__':
    print("""
    MENU:
    1 - Ajouter un nouveau plat
    2 - Choisir un plat au hasard
    """)
    choice = 0
    while choice != 1 and choice != 2:
        choice = int(input("Entrer un nombre (1-2) : "))


    if choice == 1:
        add_meal()
    if choice == 2:
        random_meal()