from tkinter import *


# creer une premiere fenetre
window = Tk()

# personnaliser cette fenetre
window.title("My Application")
window.geometry("720x480")
window.minsize(480, 360)
# window.iconbitmap("logo.ico")
window.config(background='#41B77F')

# creer la frame
frame = Frame(window, bg="#41B77F")

# ajouter un premier texte
label_title = Label(frame, text="Bienvenue sur l'application", font=("Iosevka", 32), bg='#41B77F', fg='white')
label_title.pack()

# ajouter un second texte
label_subtitle = Label(frame, text="Hey salut à tous", font=("Iosevka", 24), bg='#41B77F', fg='white')
label_subtitle.pack()

# ajouter un premier bouton
yt_button = Button(frame, text="Ouvrir Youtube", font=("Iosevka", 24), bg='white', fg='#41B77F')
yt_button.pack(pady=5, fill=X)

# ajouter
frame.pack(expand=YES)

# afficher
window.mainloop()