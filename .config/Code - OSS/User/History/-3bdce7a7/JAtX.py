import random


ENEMY_HEALTH = 50
PLAYER_HEALTH = 50
NUMBER_OF_POTIONS = 3
SKIP_TURN = False

while True:
    # Jeu du joueur
    if SKIP_TURN:
        print("Vous passez votre tour...")
        SKIP_TURN = False
    else:
        user_choice = ''
        while user_choice not in ['1', '2']:
            user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

        if user_choice == '1': # Attaquer
            your_attack = random.randint(5, 10)
            ENEMY_HEALTH -= your_attack
            print(f"Vous avez infligé {your_attack} points de dégats à l'ennemi 🪓")
        elif user_choice == '2': # Potion
            if NUMBER_OF_POTIONS > 0:
                potion_health = random.randint(15, 50)
                PLAYER_HEALTH += potion_health
                NUMBER_OF_POTIONS -= 1
                SKIP_TURN = True
                print(f"Vous récupérez {potion_health} points de vie 💝 ({NUMBER_OF_POTIONS} 🧪 restante{'s' if NUMBER_OF_POTIONS > 1 else ''})")
            else:
                print("Vous n'avez plus de potions...")

print("Fin du jeu.")