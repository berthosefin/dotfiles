

a = input("Entrez un premier nombre : ")
b = input("Entrez un deuxième nombre : ")
while not a.isdigit() and b.isdigit():
    print(f"Le resultat de l'addition de {a} avec {b} est égal à {a+b}")