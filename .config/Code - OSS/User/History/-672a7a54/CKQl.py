

while True:
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxième nombre : ")
    if a.isdigit() and b.isdigit():
        print(f"Le resultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}")
        break
    else:
        print(f"Veuillez entrer deux nombres valides")


a = b = ""

while not (a.isdigit() and b.isdigit()):
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxième nombre : ")