

word = input("Give me a word: ")
n = input("How many times should I print the result? ")
if len(word) > 2:
    if n % 2 == 0:
        print(word[-2:0])
    else:
        print(word[0:1])
else:
    print()