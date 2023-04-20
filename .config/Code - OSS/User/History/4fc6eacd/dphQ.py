

word = input("Give me a word: ")
n = int(input("How many times should I print the result? "))
if len(word) > 2:
    if n % 2 == 0:
        print(word[-2:])
    else:
        print(word[0:2])
else:
    print()