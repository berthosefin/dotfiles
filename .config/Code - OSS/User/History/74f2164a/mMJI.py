from sys import argv


try:
    age = int(argv[1])
    print(f"The captain is {age}-year-old")
except:
    print("Error: Invalid argument")
