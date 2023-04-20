import random


choix = ['Pr', 'Pp', 'Cx', 'Quit']
score_ordinateur = 0
score_joueur = 0

print("*** Le fameux 'Pièrre Papier Ciseaux' ***")
while True:
    choix_ordinateur = random.choice(choix)
    choix_joueur = ''

    while not choix_joueur in choix:
        choix_joueur = input('''Pr: Pièrre ou Pp: Papier ou Cx: Ciseaux? (Quit pour quitter) ''').capitalize()

    if choix_joueur == choix_ordinateur:
        print('EGALITE')
        continue

    elif choix_joueur == 'Pr':
        if choix_ordinateur == 'Pp':
            print("PERDU! Le papier couvre la pièrre")
            score_ordinateur += 1
        elif choix_ordinateur == 'Cx':
            print("GAGNE! La pièrre casse le ciseaux")
            score_joueur += 1
    continue

    elif choix_joueur == 'Pp':
        if choix_ordinateur == 'Pr':
            print("GAGNE! Le papier couvre la pièrre")
            score_joueur += 1
        elif choix_ordinateur == 'Cx':
            print("PERDU! Le ciseaux coupe le papier")
            score_ordinateur += 1

    elif choix_joueur == 'Cx':
        if choix_ordinateur == 'Pr':
            print("PERDU! La pièrre casse le ciseaux")
            score_ordinateur += 1
        elif choix_ordinateur == 'Pp':
            print("GAGNE! Le ciseaux coupe le papier")
            score_joueur += 1
    
    elif choix_joueur == 'Quit':
        print(f"Score de l'ordinateur: {score_ordinateur}")
        print(f"Score du joueur: {score_joueur}")

        if score_joueur > score_ordinateur:
            gagnant = '++ JOUEUR ++'
        elif score_joueur < score_ordinateur:
            gagnant = '** ORDINATEUR **'
        else:
            gagnant = '== EGALITE =='
        print(f"GAGNANT: {gagnant}")

        break

    print('-' * 50)