from sys import argv


n = argv[1]

if n.isdigit():
    if int(n) <= 20:
        pass
    else:
        raise TypeError("Must not be > 20")
else:
    raise TypeError("Must be numeric")