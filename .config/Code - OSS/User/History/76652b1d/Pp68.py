

liste = ["Pomme", "Banene"]
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
            elem_to_remove = input("Entrez le nom d'un élémént à retier de la liste de courses : ")
            if elem_to_remove in liste:
                liste.remove(elem_to_remove)
                print(f"L'élément {elem_to_remove} a bien été supprimé de la liste.")
            else:
                print(f"")
        elif choice == 3:
            if len(liste) == 0:
                print("Votre liste ne contient aucun élément.")
            else:
                print("Voici le contenu de votre liste :")
                for i,l in enumerate(liste):
                    print(f"{i+1}. {l}")
        elif choice == 4:
            print("drop_elem")
        elif choice == 5:
            print("À bientôt !")
            break
        else:
            print("Veuillez choisir un nombre entre 1 et 5")
    except:
        print("Veuillez entrer un nombre seulement")

    print("-------------------------------------------------")
    # 
    # 
    # 
        # si la liste est vide: "Votre liste ne contient aucun élément"