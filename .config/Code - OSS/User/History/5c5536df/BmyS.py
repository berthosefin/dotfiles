

phrase = "Phrase en camel case"
mots = phrase.split()
liste = [mots[0].lower()]
for mot in mots[1:]:
    liste.append(mot.capitalize())