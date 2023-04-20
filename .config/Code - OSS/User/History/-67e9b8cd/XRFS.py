

class Player:

    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print(f"Bienvenue au joueur {pseudo} / Points de vie: {health} / Attaque: {attack}")


player1 = Player("Thos", 20, 5)
player1 = Player("Birkhoff", 30, 15)