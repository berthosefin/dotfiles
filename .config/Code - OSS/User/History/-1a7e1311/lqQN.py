

while True:
    phrase = input("Parler moi: ")
    match phrase:
        case "bonjour" | "salut":
            print("Bonjour! Comment allez-vous?")