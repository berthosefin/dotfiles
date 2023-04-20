from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from subprocess import call


# Function
def login():
    username = entry_username.get()
    password = entry_password.get()
    if (username == '' or password == ''):
        messagebox.showerror('', "Il faut completer tous les champs !")
        entry_username.delete('0', 'end')
        entry_password.delete('0', 'end')
    elif (username == 'admin' and password == 'admin'):
        messagebox.showinfo('', "Bienvenue")
        entry_username.delete('0', 'end')
        entry_password.delete('0', 'end')
        root.destroy()
        call(['python', 'main.py'])
    else:
        messagebox.showwarning('', "Nom d'utiliateur ou mot de passe incorecte !")
        entry_username.delete('0', 'end')
        entry_password.delete('0', 'end')


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
entry_username = Entry(root, font=('Arial', 12))
entry_username.place(x=150, y=100, width=200, height=30)

lbl_password = Label(root, text="Mot de passe", font=('Arial', 14), bg='#2E3440', fg='#D8DEE9')
lbl_password.place(x=5, y=150, width=150)
entry_password = Entry(root, show='*', font=('Arial', 12))
entry_password.place(x=150, y=150, width=200, height=30)

# Button
btn_connect = Button(root, text="Se connecter", font=('Arial', 16), bg='#81A1C1', fg='#D8DEE9', command=login)
btn_connect.place(x=150, y=200, height=30)

# Main
root.mainloop()