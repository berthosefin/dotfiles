

# --- DEFINITION ---
class Personne:
    def __init__(self, nom = "", age = 0):
        self.nom = nom
        self.age = age
        if nom == "":
            self.nom = self.demanderNom()
        print(f"Constructeur personne {nom}")


    def sePresenter(self):
        info_personne = f"Bonjour, je m'appelle {self.nom}"
        if self.age != 0:
            info_personne += f" et j'ai {str(self.age)} ans"
        print(info_personne) 

        if self.age != 0:
            if self.estMajeur():
                print(f"Je suis majeur")
            else:
                print(f"Je suis mineur")

    
    def estMajeur(self):
        return self.age >= 18
    

    def demanderNom(self):
        self.nom = input("Quelle est votre nom ")


# --- UTILISATION ---
personne1 = Personne("Jean", 30)
personne1.sePresenter()

personne2 = Personne()
personne2.sePresenter()
