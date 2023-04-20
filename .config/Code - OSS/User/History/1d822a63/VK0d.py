from tkinter import *


# creer une premiere fenetre
window = Tk()

# personnaliser cette fenetre
window.title("My Application")
window.geometry("480x360")
window.minsize(480, 360)
# window.iconbitmap("logo.ico")
window.config(background='#41B77F')

# ajouter un premier texte
label_title = Label(window, text="Bienvenue sur l'application", font=("Courrier", 16), bg='#41B77F', fg='white')
label_title.pack()

# afficher
window.mainloop()