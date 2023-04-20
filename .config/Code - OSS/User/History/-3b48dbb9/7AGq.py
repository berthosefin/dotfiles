import random


choix = ['Pr', 'Pp', 'Cx']
choix_ordinateur = random.choice(choix)
choix_joueur = ''

while not choix_joueur in choix:
    choix_joueur = input('''Pr: Pièrre ou Pp: Papier ou Cx: Ciseaux? ''').capitalize()

if choix_joueur == choix_ordinateur:
    print('EGALITE')

elif choix_joueur == 'Pr':
    if choix_ordinateur == 'Pp':
        print("PERDU! Le papier couvre la pièrre")
    elif choix_ordinateur == 'Cx':
        print("GAGNE! La pièrre casse le ciseaux")

elif choix_joueur == 'Pp':
    if choix_ordinateur == 'Pr':
        print("GAGNE! Le papier couvre la pièrre")
    elif choix_ordinateur == 'Cx':
        print("PERDU! Le ciseaux coupe le papier")

elif choix_joueur == 'Cx':
    if choix_ordinateur == 'Pr':
        print("PERDU! La pièrre casse le ciseaux")
    elif choix_ordinateur == 'Pp':
        print("GAGNE! Le ciseaux coupe le papier")

print('-' * 50)