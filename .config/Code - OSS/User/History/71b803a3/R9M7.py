

word = input("Give us a word: ")
if word[-3:] == 'ing':
    print(f"{word}ly")
else:
    print(f"{word}ing")