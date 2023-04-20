from tkinter import *

# Window
root = Tk()
root.title("Gestion des notes")
root.geometry('1350x700+0+0')
root.resizable(False, False)
root.background('#2E3440')

# Label & Entry
lbl_title = Label(root, text="GESTION DES NOTES DES ETUDIANTS", font=('Sans Serif', 25), bg='#81A1C1', fg='#D8DEE9')
lbl_title.place(x=0, y=0, width=1350, height=100)

lbl_id = Lable(root, text="N°", font=('Arial', 18), bg='#81A1C1', fg='#D8DEE9')
lbl_id.place(x=70, y=150, width=150)
entry_id = Entry(root, font=('Arial', 12))
entry_id.place(x=250, y=150, width=150)

lbl_firstname = Lable(root, text="NOM", font=('Arial', 18), bg='#81A1C1', fg='#D8DEE9')
lbl_firstname.place(x=70, y=200, width=150)
entry_firstname = Entry(root, font=('Arial', 12))
entry_firstname.place(x=250, y=200, width=300)

lbl_lastname = Lable(root, text="PRENOM", font=('Arial', 18), bg='#81A1C1', fg='#D8DEE9')
lbl_lastname.place(x=70, y=250, width=150)
entry_lastname = Entry(root, font=('Arial', 12))
entry_lastname.place(x=250, y=250, width=300)

# Main
root.mainloop()