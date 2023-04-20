from tkinter import *


# creer la fenetre
window = Tk()
window.title("Générateur de mot de passe")
window.wm_geometry(("720x480"))
# window.iconbitmap("logo.ico")
window.config(background='#4065A4')

# creation d'image
width = 300
height = 300
img = PhotoImage(file='privacy.svg'.zoom(350).subsample(32))
canvas = Canvas()

# afficher la fenetre
window.mainloop()