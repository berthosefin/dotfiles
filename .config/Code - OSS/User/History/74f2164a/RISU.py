from sys import argv


age = argv[1]

if age.isdigit():
    print(f"The captain is {age}-year-old")