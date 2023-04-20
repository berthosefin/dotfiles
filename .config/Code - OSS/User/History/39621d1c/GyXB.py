

# Simulateur de ville
# Créer 3 classes: Immeuble, Supermarché et Banque
# Superclass Batiment
class Batiment:

    def __init__(self, adresse, nb_etages):
        self.adresse = adresse
        self.nb_etages = nb_etages

    def get_addresse(self):
        return self.adresse
    
    def get_nb_etages(self):
        return self.nb_etages


class Immeuble(Batiment):

    def __init__(self, adresse, nb_etages, nb_balcons):
        Batiment.__init__(self, adresse, nb_etages)
        self.nb_balcons = nb_balcons

    def get_nb_balcons(self):
        return self.nb_balcons


class Supermarche(Batiment):

    def __init__(self, adresse, nb_etages, nb_rayons):
        Batiment.__init__(self, adresse, nb_etages)
        self.nb_rayons = nb_rayons
    
    def get_nb_rayons(self):
        return self.nb_rayons


class Banque(Batiment):

    def __init__(self, adresse, nb_etages, nb_coffres, nom):
        Batiment.__init__(self, adresse, nb_etages)
        self.nb_coffres = nb_coffres
        self.nom = nom
    
    def get_nom(self):
        return self.nom


# 4 immeubles
immeuble1 = Immeuble("26 rue de la StT", 3, 3)
immeuble2 = Immeuble("28 rue de la StT", 5, 6)
immeuble3 = Immeuble("53 rue elios mitterand", 2, 2)
immeuble5 = Immeuble("120 rue pleiades", 8, 4)

# 2 supermarché
supermarche1 = Supermarche("27 rue de la StT", 1, 12)
supermarche2 = Supermarche("119 rue pleiades", 4, 25)

# 1 banque
banque = Banque("53 rue elios mitterand", 12, 25, "FBanque")