

# Place de cinema
# recolter l'age de la personne "Quel est votre âge ?"
age = int(input("Quel est votre âge ? "))

# prix total à payer
price = 0

# si la personne est mineur -> 7€
# si la personne est majeur - 12€
if age < 18:
    price = 1
else:
    price = 12

# souhaitez-vous du pop corn ?
pop_corn = input(f"Souhaitez-vous du pop corn ?(Oui/Non) ")

# si oui -> +5€
if pop_corn.lower() == 'oui':
    price += 5

# afficher ce prix total à payer
print('Le prix total à payer est de {price}€')