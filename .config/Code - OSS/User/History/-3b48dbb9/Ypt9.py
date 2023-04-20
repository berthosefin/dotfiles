import random


choix = ['Pr', 'Pp', 'Cx']
choix_ordinateur = random.choice(choix)
choix_joueur = input('''Pr: Pièrre ou Pp: Papier ou Cx: Ciseaux? ''').capitalize()

if choix_joueur == choix_ordinateur:
    print('Egalité')
elif choix_joueur == 'Pr':
    if choix_ordinateur == 'Pp':
        print("Vous perdez, le papier couvre la pièrre")