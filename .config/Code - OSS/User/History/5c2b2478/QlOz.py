

# Window
root = Tk()
root.title("Gestion des notes")
root.geometry('1350x700+0+0')
root.resizable(False, False)
root.background('#2E3440')

# Label & Entry
lbl_title = Label(root, text="GESTION DES NOTES DES ETUDIANTS", font=('Sans Serif', 25), bg='#81A1C1', fg='#D8DEE9')
lbl_title.place(x=0, y=0, width=1350, height=100)

# Main
root.mainloop()