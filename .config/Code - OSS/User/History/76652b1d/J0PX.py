

liste = []
while True:
    print('''
    Choisissez parmi les 5 options suivantes : 
    1: Ajouter un élément à la liste
    2: Retirer un élément de la liste
    3: Afficher la liste
    4: Vider la liste
    5: Quitter
    ''')
    try:
        choice = int(input("Votre choix : "))
        if choice == 1:
            print("add_elem")
        elif choice == 2:
            print("remove_elem")
        elif choice == 3:
            print("print_elem")
        elif choice == 4:
            print("drop_elem")
        elif choice == 5:
            print("À bientôt !")
            break
        else:
            print("Veuillez choisir un nombre entre 1 et 5")
    except:
        print("Veuillez choisir un nombre entre 1 et 5")

    print("-------------------------------------------------")
    # 
    # 
    # 
        # si la liste est vide: "Votre liste ne contient aucun élément"