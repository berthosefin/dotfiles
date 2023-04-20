

class Player:

    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print(f"Bienvenue au joueur {pseudo} /Points de vie: {health} /Attaque: {attack}")
    
    def get_pseudo(self):
        return self.pseudo
    
    def get_health(self):
        return self.health
    
    def get_attack_value(self):
        return self.attack

    def set_weapon(self, weapon):
        self.health = weapon
        return self.health
    
    def damage(self, damage):
        self.health -= damage
    
    def attack_player(self, target_player):
        target_player.damage(self.attack)