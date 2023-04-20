from sys import argv


n = argv[1]

if n.isdigit():
    pass
else:
    raise TypeError("Must be numeric")