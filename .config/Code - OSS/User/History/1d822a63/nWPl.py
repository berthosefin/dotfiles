from tkinter import *


# creer une premiere fenetre
window = Tk()

# personnaliser cette fenetre
window.title("My Application")
window.geometry("480x360")
window.minsize(480, 360)
# window.iconbitmap("logo.ico")
window.config(background='#41B77F')

# creer la frame
frame = Frame(window, bg="red", bd=1, relief=SUNKEN)

# ajouter un premier texte
label_title = Label(frame, text="Bienvenue sur l'application", font=("Arial", 16), bg='#41B77F', fg='white')

# ajouter un second texte
label_subtitle = Label(frame, text="Hey salut à tous", font=("Arial", 14), bg='#41B77F', fg='white')

# ajouter
frame.pack(expand=YES)

# afficher
window.mainloop()