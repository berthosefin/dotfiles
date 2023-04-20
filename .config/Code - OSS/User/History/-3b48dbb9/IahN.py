import random


choix = ['Pr', 'Pp', 'Cx']
choix_ordinateur = random.choice(choix)
choix_joueur = input('''Pr: Pièrre ou Pp: Papier ou Cx: Ciseaux? ''').capitalize()

if choix_joueur == choix_ordinateur:
    print('EGALITE')

elif choix_joueur == 'Pr':
    if choix_ordinateur == 'Pp':
        print("PERDU! Le papier couvre la pièrre")
    elif choix_ordinateur == 'Cx':
        print("GAGNE! Le papier couvre la pièrre")

elif choix_joueur == 'Pp':
    if choix_ordinateur == 'Pp':
        print("PERDU! Le papier couvre la pièrre")
    elif choix_ordinateur == 'Cx':
        print("GAGNE! Le papier couvre la pièrre")