import random


choix = ['Pr', 'Pp', 'Cx']
choix_ordinateur = random.choice(choix)
choix_joueur = input('''Pr: Pièrre ou Pp: Papier ou Cx: Ciseaux? ''').capitalize()