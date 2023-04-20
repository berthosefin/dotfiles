

class Player:

    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print(f"Bienvenue au guerrier {pseudo} /Point de vie: {health} /Attaque: {attack}")
    
    def get_pseudo(self):
        return self.pseudo
    
    def get_health(self):
        return self.health
    
    def get_attack_value(self):
        return self.attack
    
    def damage(self, damage):
        self.health -= damage
    
    def attack_player(self, target_player):
        target_player.damage(self.attack)


class Warrior(Player):

    def __init__(self, pseudo, health, attack):
        self.armor  = 3
        print(f"Bienvenue au joueur {pseudo} /Point de vie: {health} /Attaque: {attack}")
    
    def damage(self, damage):
        pass
    
    def attack_player(self, target_player):
        target_player.damage(self.attack)
    
    def blade(self):
        self.armor = 3
        print("Les points d'armure ont été rechargé")
    
    def get_armor_point(self):
        return self.armor
    

player = Player('Thos', 20, 2)
player.damage(3)

warrior = Warrior("DarkWarrior", 30, 4)
warrior.damage(4)
print(f"vie: {warrior.get_health()}, armure: {warrior.get_armor_point()}")