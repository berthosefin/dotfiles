from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from subprocess import call


# Window
root = Tk()
root.title("Connexion")
root.geometry('400x300+450+200')
root.resizable(False, False)
root.configure(background='#2E3440')

# Title
lbl_title = Label(root, text="Connexion", font=('Arial', 25), bg='#81A1C1', fg='#D8DEE9')
lbl_title.place(x=0, y=0, width=400)

lbl_username = Label(root, text="Nom d'utilisateur", font=('Arial', 14), bg='#2E3440', fg='#D8DEE9')
lbl_username.place(x=5, y=100, width=150)

# Execution
root.mainloop()