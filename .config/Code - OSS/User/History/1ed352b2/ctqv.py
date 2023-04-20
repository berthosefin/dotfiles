

doubled = "nspl"
sentence = input("Enter a sentence: ")
new_sentence = ""
for s in sentence:
    if s in doubled:
        new_sentence.append(s*2)
    else:
        new_sentence.append(s)
print(new_sentence)
    