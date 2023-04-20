

class Player:

    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print(f"Bienvenue au joueur {pseudo} / Points de vie: {health} / Attaque: {attack}")
    
    def get_pseudo(self):
        return self.pseudo
    
    def get_health(self):
        return self.health
    
    def get_attack_value(self):
        return self.attack
    
    def damage(self, damage):
        self.health -= damage
        print(f"Aie...vous venez de subir {damage} dégats!")
        print(f"Vous possedez désormais {self.get_health()}\n")
    
    def attack_player(self, target_player):
        target_player.damage(self.get_attack_value)


player1 = Player("Thos", 20, 5)
player2 = Player("Birkhoff", 30, 15)

player1.attack_player(player2)
print(f"{player1.get_pseudo()} attaque {player2.get_pseudo}")

print(f"{player1.get_pseudo()}\n  -Points de vie: {player1.get_health()}\n  -Attaque: {player1.get_attack_value()}\n")
print(f"{player2.get_pseudo()}\n  -Points de vie: {player2.get_health()}\n  -Attaque: {player2.get_attack_value()}\n")
