

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

    def __init__(self):
        super().__init__()


class Supermarché(Batiment):

    def __init__(self):
        super().__init__()


class Banque(Batiment):

    def __init__(self):
        super().__init__()
        

# 4 immeubles, 2 supermarché et 1 banque