

def quest(q):
    global score
    print(q[0])
    for i in range(len(q[1])):
        print(f"{i+1} - {q[1][i]}")
    print()
    resp = input("Votre réponse: ")
    if resp.lower() == q[2].lower():
        print("Bonne réponse.")
        score += 1
    else:
        print("Mauvaise réponse.")
    print()


score = 0
q1 = ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris")
q2 = ("Quelle est la capitale de Madagascar ?", ("Toamasina", "Antananarivo", "Fianarantsoa", "Toliara"), "Antananarivo")
q3 = ("Quelle est la capitale de l'Italie ?", ("Rome", "Naple", "Florence", "Venise"), "Rome")
q4 = ("Quelle est la capitale de l'Espagne ?", ("Barcelona", "Madrid", "Seville", "Autres"), "Autres")

quest(q1)
quest(q2)
quest(q3)
quest(q4)

print(f"Score Final: {score}")