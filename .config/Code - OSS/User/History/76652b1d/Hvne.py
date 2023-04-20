

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
    choice = input("Votre choix : ")
    match choice:
        case 1:
            add_elem()
        case 2:
            remove_elem()
        case 3:
            print_elem()
        case 4:
            drop_elem()
        case 5:
            print("À bientôt !")
            break
    # 
    # 
    # 
        # si la liste est vide: "Votre liste ne contient aucun élément"
    # 
    # 
        # 
    # Votre choix : 3