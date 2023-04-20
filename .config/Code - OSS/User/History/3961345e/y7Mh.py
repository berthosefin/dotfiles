

# tp : une fonction pour calculer le nombre de voyelles dans un mot
# definir une fonction get_vowels_numbers(mot)
def get_vowels_numbers(words):
    # créer un compte de voyelles
    c = 0

    # pour chaque lettre du mot vous verifiez s'il s'agit d'un voyelle
    for w in words:
        if w in 'aeyuio':
            c += 1
# si c'est le cas, on ajoute un au compteur
# à la fin de la fonction, vous allez renvoyer le compteur