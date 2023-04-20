from sys import argv

try:
    n = int(argv[1])
    if n <= 20:
        pass
    else:
        raise TypeError("Must not be > 20")
except TypeError:
    print("Must not be > 20")