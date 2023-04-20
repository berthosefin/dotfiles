from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3


def add_patient():
    id_p = entry_id_p.get()
    firstname = entry_firstname.get()
    lastname = entry_lastname.get()
    age = entry_age.get()
    address = entry_address.get()
    phone = entry_phone.get()
    remark = entry_remark.get()

    # SQlite connexion
    con = sqlite3.connect('hospital.db')
    curs = con.cursor()
    curs.execute("INSERT INTO patient('id_p', 'firstname', 'lastname', 'age', 'address', 'phone', 'remark') VALUES(?,?,?,?,?,?,?)")
    con.commit()
    con.close()
    messagebox.showinfo("Patient ajouter")

    # Print
    con = sqlite3.connect('hospital.db')
    curs = con.cursor()
    select = curs.execute("SELECT * FROM patient ORDER BY id DESC")
    select = list(select)
    table.insert('', END, values = select[0])
    con.close()


def edit_patient():
    id_p = entry_id_p.get()
    firstname = entry_firstname.get()
    lastname = entry_lastname.get()
    age = entry_age.get()
    address = entry_address.get()
    phone = entry_phone.get()
    remark = entry_remark.get()

    # SQlite connexion
    con = sqlite3.connect('hospital.db')
    curs = con.cursor()
    curs.execute(
        "UPDATE patient SET firstname=?, lastname=?, age=?, address=?, phone=?, remark=? WHERE id_p=?",
        (firstname, lastname, age, address, phone, remark, id_p))
    con.commit()
    con.close()
    messagebox.showinfo("Patient modifier")

    # Print
    con = sqlite3.connect('hospital.db')
    curs = con.cursor()
    select = curs.execute("SELECT * FROM patient ORDER BY id DESC")
    select = list(select)
    table.insert('', END, values = select[0])
    con.close()


def remove_patient():
    id_p_selected = table.item(table.selection())['values'][0]
    con = sqlite3.connect('hospital.db')
    curs = con.cursor()
    delete = curs.execute(f"DELETE FROM patient WHERE id_p = {id_p_selected}")
    con.commit()
    table.delete(table.selection())


# Main
root = Tk()
root.title('Gestion des patients')
root.geometry('1300x700')

# Title
lbl_title = Lable(root, text="GESTION DES PATIENTS CHE THopital", font=(Arial, 30), bg='#81A1C1', fg='#D8DEE9')
lbl_title.place(x=0, y=0, width=1365)

lbl_list = Label(root, text="LISTE DES PATIENTS", font=(Arial, 16), bg='#81A1C1', fg='#D8DEE9')
lbl_list.place(x=600, y=100, width=760)

# ID
lbl_id_p = Label(root, text="N°", font=(Arial, 16, ), bg='#A3BE8C', fg='#D8DEE9')
lbl_id_p.place(x=0, y=100, width=200)
entry_id_p = Entry(root)
entry_id_p.place(x=200, y=100, width=160, height=30)

# Firstname
lbl_firstname = Label(root, text="Nom", font=(Arial, 16, ), bg='#A3BE8C', fg='#D8DEE9')
lbl_firstname.place(x=0, y=150, width=200)
entry_firstname = Entry(root)
entry_firstname.place(x=200, y=150, width=200, height=30)

# Lastname
lbl_lastname = Label(root, text="Prenom", font=(Arial, 16, ), bg='#A3BE8C', fg='#D8DEE9')
lbl_lastname.place(x=0, y=200, width=200)
entry_lastname = Entry(root)
entry_lastname.place(x=200, y=200, width=200, height=30)

# Age
lbl_age = Label(root, text="Age", font=(Arial, 16, ), bg='#A3BE8C', fg='#D8DEE9')
lbl_age.place(x=0, y=250, width=200)
entry_age = Entry(root)
entry_age.place(x=200, y=250, width=200, height=30)

# Address
lbl_address = Label(root, text="Addresse", font=(Arial, 16, ), bg='#A3BE8C', fg='#D8DEE9')
lbl_address.place(x=0, y=300, width=200)
entry_address = Entry(root)
entry_address.place(x=200, y=300, width=200, height=30)

# Phone
lbl_phone = Label(root, text="Téléphone", font=(Arial, 16, ), bg='#A3BE8C', fg='#D8DEE9')
lbl_phone.place(x=0, y=350, width=200)
entry_phone = Entry(root)
entry_phone.place(x=200, y=350, width=200, height=30)

# remark
lbl_remark = Label(root, text="Rémarque", font=(Arial, 16, ), bg='#A3BE8C', fg='#D8DEE9')
lbl_remark.place(x=0, y=400, width=200)
entry_remark = Entry(root)
entry_remark.place(x=200, y=400, width=200, height=30)

# Button
btn_register = Button(root, text="Enregistrer", font=(Arial, 16), bg='#81A1C1', fg='#D8DEE9', command=add_patient)
btn_register.place(x=30, y=450, width=200)

btn_edit = Button(root, text="Modifier", font=(Arial, 16), bg='#81A1C1', fg='#D8DEE9', command=edit_patient)
btn_edit.place(x=270, y=450, width=200)

btn_remove = Button(root, text="Supprimer", font=(Arial, 16), bg='#81A1C1', fg='#D8DEE9', command=remove_patient)
btn_remove.place(x=150, y=500, width=200)

# Table
