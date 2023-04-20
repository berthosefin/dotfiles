

VOWELS = ("a", "e", "i", "o", "u")
sentence = input("Enter a sentence: ")
for s in sentence:
    if not s in VOWELS:
        print(s)