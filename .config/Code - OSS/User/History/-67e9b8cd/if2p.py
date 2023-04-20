from model.player import Player
from model.weapon import Weapon


knife = Weapon('Couteau', 3)
player1 = Player("Thos", 20, 3)

# donne un couteau faisant 3 dégats au joueur !
player1.set_weapon(knife)
player2 = Player("Birkhoff", 20, 5)

player1.attack_player(player2)
print(f"{player1.get_pseudo()} attaque {player2.get_pseudo()}")

print(f"Joueur {player1.get_pseudo()} / Points de vie: {player1.get_health()} / Attaque: {player1.get_attack_value()}")
print(f"Joueur {player2.get_pseudo()} / Points de vie: {player2.get_health()} / Attaque: {player2.get_attack_value()}")
