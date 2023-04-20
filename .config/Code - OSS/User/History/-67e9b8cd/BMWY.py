from model.player import Player


player1 = Player("Thos", 20, 5)
player2 = Player("Birkhoff", 30, 15)

player1.attack_player(player2)
print(f"{player1.get_pseudo()} attaque {player2.get_pseudo()}")

print(f"{player1.get_pseudo()} / Points de vie: {player1.get_health()} / Attaque: {player1.get_attack_value()}")
print(f"{player2.get_pseudo()} / Points de vie: {player2.get_health()} / Attaque: {player2.get_attack_value()}")
