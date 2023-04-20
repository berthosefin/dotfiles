

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


class Supermarché(Batiment):

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


# 4 immeubles, 2 supermarché et 1 banque