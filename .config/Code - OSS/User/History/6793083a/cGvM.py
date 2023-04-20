

CONST = 42
user_input = -1
while user_input < 0:
    try:
        user_input = int(input("Entrer un nombre positive: "))
    except ValueError:
        print("Vous devez rentrer un nombre!!! Veillez réessayez")

if user_input < CONST:
    print(CONST - user_input)
elif user_input >= CONST:
    print((user_input - CONST)*2)