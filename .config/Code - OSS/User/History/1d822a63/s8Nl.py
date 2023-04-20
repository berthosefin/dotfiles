from tkinter import *


# creer une premiere fenetre
window = Tk()

# personnaliser cette fenetre
window.title("My Application")
window.geometry("1080x720")
window.minsize(480, 360)
# window.iconbitmap("logo.ico")
window.config(background='#41B77F')

# afficher
window.mainloop()