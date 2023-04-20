

VOWELS = ("a", "e", "i", "o", "u")
sentence = input("Enter a sentence: ")
for s in sentence:
    if s in VOWELS:
        continue
    print(s)