

def accro_gen(sentence):
    words = sentence.split()
    accro = ''
    for i in words:
        accro += i[0].upper()
    res = accro

sentence = input("Donner une chaine de caractère: ")
res = accro_gen(sentence)
print(f"Voici l'accronyme de {sentence}: {res}")


