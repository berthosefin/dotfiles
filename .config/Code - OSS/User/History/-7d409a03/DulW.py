

# --- DEFINITION ---
class Personne:
    ESPECE_ETRE_VIVANT = "Humain"   # variable de class

    def __init__(self, nom = "", age = 0):
        self.nom = nom  # variable d'instance
        self.age = age
        if nom == "":
            self.demanderNom()
        print(f"Constructeur personne {self.nom}")


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
liste_personnes = [Personne("Jean", 30),
                    Personne("Paul", 4),
                    Personne("Pierre")]

for personne in liste_personnes:
   personne.sePresenter()
   print()
