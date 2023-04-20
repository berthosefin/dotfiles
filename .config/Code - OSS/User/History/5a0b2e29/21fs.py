

sentence = input("Donner une chaine de caractère: ")
words = sentence.split()
accr = ''
for i in words:
    accr += i[0].upper()
print(accr)

