

phrase = "Phrase en camel case"
mots = phrase.split()
liste = [mots.pop(0).lower()]
for mot in mots:
    liste.append(mot.capitalize())
resultat = "".join(liste)