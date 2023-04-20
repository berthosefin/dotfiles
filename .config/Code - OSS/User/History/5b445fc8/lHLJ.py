from sys import argv


n = argv[1]

if n.isdigit() and n <= 20:
    pass
elif int(n) > 20:
    raise TypeError("Must not be > 20")
else:
    raise TypeError("Must be numeric")