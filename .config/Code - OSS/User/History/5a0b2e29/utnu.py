

sentence = input("Donner une chaine de caractère: ")
words = sentence.split(' ')
print(words)
for w in words:
    acc = words[w][1].upper()
