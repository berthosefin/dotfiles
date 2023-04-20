

class Player:

    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print(f"Bienvenue au joueur {pseudo}\n  -Points de vie: {health}\n  -Attaque: {attack}\n")
    
    def get_pseudo(self):
        return self.pseudo
    
    def get_health(self):
        return self.health
    
    def get_attack(self):
        return self.attack
    
    def damage(self, damage):
        self.health -= damage
        print(f"Aie...vous venez de subir {damage} dégats!")
        print(f"Vous possedez désormais {self.get_health()}\n")


player1 = Player("Thos", 20, 5)
player1.damage(5)

player1 = Player("Birkhoff", 30, 15)