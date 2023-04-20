

# CONST = 42
# user_input = -1
# while user_input < 0:
#     try:
#         user_input = int(input("Entrer un nombre positive: "))
#     except ValueError:
#         print("Vous devez rentrer un nombre!!! Veillez réessayez")

# if user_input < CONST:
#     print(CONST - user_input)
# elif user_input >= CONST:
#     print((user_input - CONST)*2)

CONST = 42
nbr_str = ""
while not nbr_str.is_digit() and int(nbr_str) < 0:
    user_input = input("Entrer un nombre positive: ")

nbr_int = int(nbr_str)
if nbr_int < CONST:
    print(CONST - nbr_int)
elif nbr_int >= CONST:
    print((nbr_int - CONST)*2)