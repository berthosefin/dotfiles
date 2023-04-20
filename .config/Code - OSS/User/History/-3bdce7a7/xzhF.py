from random import randint


user_health = 50
user_potion = 3
enemy_health = 50

while user_health > 0 and enemy_health > 0:
    user_input = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

    while not user_input == '1' and user_input == '2':
        user_input = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

    if user_input == '1':
        user_attack = randint(5, 10)
        enemy_attack = randint(5, 15)
        user_health -= enemy_attack
        enemy_health -= user_attack
        print(f"Vous avez infligé {user_attack} points de dégats à l'ennemi 🪓")
        print(f"L'ennemi vous a infligé {enemy_attack} points de dégats 🪓")
    elif user_input == '2':
        user_potion -= 1
        potion = randint(15, 50)
        enemy_attack = randint(5, 15)
        user_health -= enemy_attack
        print(f"Vous récupérez {potion} points de vie 💝 ({user_potion} 🧪 restante{'s' if user_potion > 1 else ''})")
        print(f"L'ennemi vous a infligé {enemy_attack} points de dégats 🪓")
    
    print(f"Il vous reste {user_health} point{'s' if user_health > 1 else ''} de vie.")
    print(f"Il reste {enemy_health} point{'s' if enemy_health > 1 else ''} de vie à l'ennemi.")

print('-' * 50)