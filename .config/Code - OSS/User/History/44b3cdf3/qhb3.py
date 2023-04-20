

def ask_for_number(min, max):
    response_str = input(f"Votre réponse {min} et {max}): ")
    try:
        response_int = int(response_str)
        if min <= response_int <= max:
            return response_int
        else:
            print(f"ERREUR: Vous devez renter un nombre entre {min} et {max}")
    except:
        print("ERREUR: Veillez rentrer uniquement des chiffres.")
    return ask_for_number(min, max)


def question(q):
    title = q[0]
    choice = q[1]
    good_choice = q[2]
    global score
    print(title)
    for i in range(len(choice)):
        print(f"    {i+1} - {choice[i]}")
    print()
    response = ask_for_number(1, len(choice))
    if choice[response-1].lower() == good_choice.lower():
        print("Bonne réponse.")
        score += 1
    else:
        print("Mauvaise réponse.")
    print()


def run_question(quest):
    for q in quest:
        question(q)


score = 0
q = (("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris"),
    ("Quelle est la capitale de Madagascar ?", ("Toamasina", "Antananarivo", "Fianarantsoa", "Toliara"), "Antananarivo"),
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Naple", "Florence", "Venise"), "Rome"),
    ("Quelle est la capitale de l'Espagne ?", ("Barcelona", "Madrid", "Seville", "Autres"), "Autres"))

run_question(q)

print(f"Score Final: {score}")