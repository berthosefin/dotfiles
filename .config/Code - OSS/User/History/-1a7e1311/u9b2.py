

while True:
    phrase = input("Parler moi: ")
    match phrase:
        case "bonjour" | "salut":
            print("Bonjour! Comment allez-vous ?")
        case "bien":
            print("Je vais bien aussi")
        case "bye":
            print("Au revoir")
            break
        case _:
            print("J'ai rien compris")