

class Weapon:
    
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    
    def get_name(self):
        return self.name
    
    def get_damage_amount(self):
        return self.damage