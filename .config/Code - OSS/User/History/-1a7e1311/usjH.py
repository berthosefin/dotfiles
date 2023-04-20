

# while True:
#     phrase = input("Parler moi: ")
#     match phrase:
#         case "bonjour" | "salut":
#             print("Bonjour! Comment allez-vous ?")
#         case "bien":
#             print("Je vais bien aussi")
#         case "bye":
#             print("Au revoir")
#             break
#         case _:
#             print("Je n'ai compris")


# personne1 = {"nom": "Paul", "infos": (30, "Fisc")}
# personne2 = {"nom": "Jean", "age": 25, "metier": "Etudiant"}
# personne3 = {"nom": "Nick", "age": 37}
# personne4 = {"nom": "Anna", "age": 17}
# personne5 = {"age": 17}

# personnes = (personne1, personne2, personne3, personne4, personne5)

# for personne in personnes:
#     match personne:
#         case {"nom": nom, "infos": (age, metier)}:
#             print(f"{nom}, {age} ans, {metier}")
#         case {"nom": nom, "age": age, "metier": metier}:
#             print(f"{nom}, {age} ans, {metier}")
#         case {"nom": nom, "age": age} if age >= 18:
#             print(f"{nom}, {age} ans")
#         case {"nom": nom, "age": age}:
#             print(f"{nom}, {age} ans (mineur)")
#         case _:
#             print("Format inconnu")
        
        
