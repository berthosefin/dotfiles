from sys import argv


age = argv[1]

if isinstance(age, int):
    print(f"The captain is {age}-year-old")