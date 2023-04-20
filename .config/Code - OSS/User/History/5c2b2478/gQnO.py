from tkinter import *
from tkinter import ttk

# Window
root = Tk()
root.title("Gestion des notes")
root.geometry('1350x700+0+0')
root.resizable(False, False)
root.configure(background='#2E3440')

# Label & Entry
lbl_title = Label(root, text="GESTION DES NOTES DES ETUDIANTS", font=('Sans Serif', 25), bg='#81A1C1', fg='#D8DEE9')
lbl_title.place(x=0, y=0, width=1350, height=100)

lbl_id = Label(root, text="N°", font=('Arial', 18), bg='#81A1C1', fg='#D8DEE9')
lbl_id.place(x=70, y=150, width=150)
entry_id = Entry(root, font=('Arial', 14))
entry_id.place(x=250, y=150, width=150)

lbl_firstname = Label(root, text="NOM", font=('Arial', 18), bg='#81A1C1', fg='#D8DEE9')
lbl_firstname.place(x=70, y=200, width=150)
entry_firstname = Entry(root, font=('Arial', 14))
entry_firstname.place(x=250, y=200, width=300)

lbl_lastname = Label(root, text="PRENOM", font=('Arial', 18), bg='#81A1C1', fg='#D8DEE9')
lbl_lastname.place(x=70, y=250, width=150)
entry_lastname = Entry(root, font=('Arial', 14))
entry_lastname.place(x=250, y=250, width=300)

gender = StringVar()
lbl_gender_m = Radiobutton(root, text="MASCULIN", value='M', variable=gender, indicatoron=0, font=('Arial', 14), bg='#4C566A', fg='#D8DEE9')
lbl_gender_m.place(x=250, y=300, width=150)
lbl_gender_f = Radiobutton(root, text="FEMININ", value='F', variable=gender, indicatoron=0, font=('Arial', 14), bg='#4C566A', fg='#D8DEE9')
lbl_gender_f.place(x=420, y=300, width=150)

lbl_level = Label(root, text="CLASSE", font=('Arial', 18), bg='#81A1C1', fg='#D8DEE9')
lbl_level.place(x=70, y=350, width=150)

combo_level = ttk.Combobox(root, font=('Arial', 14))
combo_level['values'] = ['L1', 'L2', 'L3', 'M1', 'M2', 'D1', 'D2', 'D3']
combo_level.place(x=250, y=350, width=150)

lbl_ue = Label(root, text="MATIERE", font=('Arial', 18), bg='#81A1C1', fg='#D8DEE9')
lbl_ue.place(x=70, y=400, width=150)
entry_ue = Entry(root, font=('Arial', 14))
entry_ue.place(x=250, y=400, width=300)

lbl_note = Label(root, text="NOTE", font=('Arial', 18), bg='#81A1C1', fg='#D8DEE9')
lbl_note.place(x=70, y=450, width=150)
entry_note = Entry(root, font=('Arial', 14))
entry_note.place(x=250, y=40, width=200)

# Main
root.mainloop()