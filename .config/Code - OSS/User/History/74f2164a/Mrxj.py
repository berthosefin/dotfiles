from sys import argv


age = argv[1]

try:
    print(f"The captain is {age}-year-old")
except:
    print("Error: Invalid argument")
