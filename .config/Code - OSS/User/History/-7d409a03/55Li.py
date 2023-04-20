

# --- DEFINITION ---
class Personne:
    def __init__(self, nom = "", age = 0):
        if nom == "":
            self.nom = self.demanderNom()
        else:
            self.nom = nom
        self.age = age
        print(f"Constructeur personne {nom}")


    def sePresenter(self):
        information = f"Bonjour, je m'appelle {self.nom}"
        if not self.age == 0:
            print(f"{presentation} et j'ai {str(self.age)} ans")
            if self.estMajeur():
                print(f"Je suis majeur")
            else:
                print(f"Je suis mineur")
        else:
            print(presentation) 

    
    def estMajeur(self):
        return self.age >= 18
    

    def demanderNom(self):
        nom = input("Quelle est votre nom ")
        return nom


# --- UTILISATION ---
personne1 = Personne("Jean", 30)
personne1.sePresenter()

personne2 = Personne()
personne2.sePresenter()
