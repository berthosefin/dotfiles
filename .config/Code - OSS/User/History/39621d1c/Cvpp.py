

class Player:

    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print(f"Bienvenue au joueur {pseudo} /Point de vie: {health} /Attaque: {attack}")