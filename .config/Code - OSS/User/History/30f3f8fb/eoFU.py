import os
import random
from tkinter import *


def generate_random_meal_suggestion():
    if os.path.exists("meals.txt"):
        with open("meals.txt", "r") as file:
            meal_random_choice = random.choice(file.readlines())
            random_meal_title.config(text=meal_random_choice, font=("Helvetica", 20), bg="#E9EA81", fg="#223E44")
    else:
        print("La ressource meals.txt n'existe pas")


# creer la fenetre
window = Tk()
window.title("Qu'allons nous manger ?")
window.geometry("720x480")
window.config(background='#E9EA81')

# creer la frame principale
frame = Frame(window, bg="#E9EA81")

# creer un titre
label_title = Label(frame, text="Qu'allons nous manger ?", font=("Helvetica", 20), bg="#E9EA81", fg="#223E44")
label_title.pack()

# choix au hasard
random_meal_title = Label(frame, text="Soupe", font=("Helvetica", 20), bg="#E9EA81", fg="#223E44")
random_meal_title.pack()

# creer un bouton
generate_password_button = Button(frame, text="Je sais pas", font=("Helvetica", 20), bg="#E9EA81", fg="#223E44",  command=generate_random_meal_suggestion)
generate_password_button.pack(fill=X)

# afficher la frame
frame.pack(expand=YES)

# afficher la fenetre
window.mainloop()