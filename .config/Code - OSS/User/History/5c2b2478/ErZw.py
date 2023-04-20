from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from subprocess import call
import mysql.connector


# Function
def register_student():
    id_s = entry_id_s.get()
    firstname = entry_firstname.get()
    lastname = entry_lastname.get()
    gender = entry_gender.get()
    level = entry_level.get()
    ue = entry_ue.get()
    note = entry_note.get()

    con = mysql.connector.connect(host='localhost', user='birkhoff', password="Bertho'f1", database='students')
    curs = con.cursor()

    try:
        sql = "INSERT INTO students (id, firstname, lastname, gender, level, ue, note) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (id_s, firstname, lastname, gender, level, ue, note)
        curs.execute(sql, val)
        con.commit()
        last_id_s = curs.lastrowid
        messagebox.showinfo('Info', 'Note ajouter')
        root.destroy()
        call(['python', 'main.py'])
    except Exception as e:
        print(e)
        con.rollback()
        con.close()


def edit_student():
    id_s = entry_id_s.get()
    firstname = entry_firstname.get()
    lastname = entry_lastname.get()
    gender = entry_gender.get()
    level = entry_level.get()
    ue = entry_ue.get()
    note = entry_note.get()

    con = mysql.connector.connect(host='localhost', user='birkhoff', password="Bertho'f1", database='students')
    curs = con.cursor()

    try:
        sql = "UPDATE note SET firstname=%s, lastname=%s, gender=%s, level=%s, ue=%s, note=%s, WHERE id=%s"
        val = (firstname, lastname, gender, level, ue, note, id_s)
        curs.execute(sql, val)
        con.commit()
        last_id_s = curs.lastrowid
        messagebox.showinfo('Info', 'Note modifier')
        root.destroy()
        call(['python', 'main.py'])
    except Exception as e:
        print(e)
        con.rollback()
        con.close()


def delete_student():
    id_s = entry_id_s.get()

    con = mysql.connector.connect(host='localhost', user='birkhoff', password="Bertho'f1", database='student')
    curs = con.cursor()


# Window
root = Tk()
root.title("Gestion des notes")
root.geometry('1350x700+0+0')
root.resizable(False, False)
root.configure(background='#2E3440')

# Label & Entry
lbl_title = Label(root, text="GESTION DES NOTES DES ETUDIANTS", font=('Sans Serif', 25), bg='#81A1C1', fg='#D8DEE9')
lbl_title.place(x=0, y=0, width=1350, height=100)

lbl_id_s = Label(root, text="N°", font=('Arial', 18), bg='#81A1C1', fg='#D8DEE9')
lbl_id_s.place(x=70, y=150, width=150)
entry_id_s = Entry(root, font=('Arial', 14))
entry_id_s.place(x=250, y=150, width=150)

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
entry_note.place(x=250, y=450, width=200)

# Button
btn_register = Button(root, text="Enregistrer", font=('Arial', 16), bg='#A3BE8C', fg='#D8DEE9', command=register_student)
btn_register.place(x=250, y=500, width=200)

btn_edit = Button(root, text="Modifier", font=('Arial', 16), bg='#81A1C1', fg='#D8DEE9', command=edit_student)
btn_edit.place(x=250, y=550, width=200)

btn_delete = Button(root, text="Supprimer", font=('Arial', 16), bg='#BF616A', fg='#D8DEE9', command=delete_student)
btn_delete.place(x=250, y=600, width=200)

# Table
table = ttk.Treeview(root, columns=(1,2,3,4,5,6,7), height=5, show='headings')
table.place(x=560, y=150, width=790, height=450)

# Head
table.heading(1, text='N°')
table.heading(2, text='NOM')
table.heading(3, text='PRENOM')
table.heading(4, text='SEXE')
table.heading(5, text='NIVEAU')
table.heading(6, text='UE')
table.heading(7, text='NOTE')

# Columns
table.column(1, width=50)
table.column(2, width=150)
table.column(3, width=150)
table.column(4, width=100)
table.column(5, width=50)
table.column(6, width=100)
table.column(7, width=50)

# Print unfo
con = mysql.connector.connect(host='localhost', user='birkhoff', password="Bertho'f1", database='students')
curs = con.cursor()
curs.execute("SELECT * FROM student")
for row in curs:
    table.insert('', END, value=row)
con.close()

# Main
root.mainloop()