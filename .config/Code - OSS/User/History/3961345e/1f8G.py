

# tp : une fonction pour calculer le nombre de voyelles dans un mot
# definir une fonction get_vowels_numbers(mot)
def get_vowels_numbers(words):
    # créer un compte de voyelles
    c = 0

    # pour chaque lettre du mot vous verifiez s'il s'agit d'un voyelle
    # si c'est le cas, on ajoute un au compteur
    for w in words:
        if w in 'aeyuio':
            c += 1

    # à la fin de la fonction, vous allez renvoyer le compteur
    print(f"Nombre des voyelles: {c}")