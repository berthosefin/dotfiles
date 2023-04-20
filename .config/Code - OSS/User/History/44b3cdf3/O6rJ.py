

def question(q):
    title = q[0]
    choice = q[1]
    good_choice = q[2]
    global score
    print(title)
    for i in range(len(choice)):
        print(f"{i+1} - {choice[i]}")
    print()
    response = input(f"Votre réponse (entre 1 et {len(choice)}): ")
    if response.lower() == good_choice.lower():
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

question(q1)
question(q2)
question(q3)
question(q4)

print(f"Score Final: {score}")