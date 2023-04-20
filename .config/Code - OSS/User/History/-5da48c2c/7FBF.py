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
lbl_title = Label(root, text="Connexion", font=('Arial', 14), bg='#81A1C1', fg='#D8DEE9')

# Execution
root.mainloop()