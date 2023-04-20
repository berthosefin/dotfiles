

word = input("Give me a word: ")
try:
    n = int(input("How many times should I print the result?(number) "))
except:
    print("Enter a number please!!!")
    
if len(word) > 2:
    if n % 2 == 0:
        print(word[-2:])
    else:
        print(word[0:2])
else:
    print()