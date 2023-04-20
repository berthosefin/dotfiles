

n = 0
while n == 0:
    big_input = input("Give me an input with more than 10 chars: ")
    if len(big_input) > 10:
        n += 1
    print("Thanks!")