

sentence = input("Donner une chaine de caractère: ")

def accro_gen(sentence):
    words = sentence.split()
    accro = ''
    for i in words:
        accro += i[0].upper()
    print(f"Voici l'accronyme de {sentence}: {accro}")

accro_gen(sentence)


