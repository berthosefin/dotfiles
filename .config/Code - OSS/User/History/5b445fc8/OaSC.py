from sys import argv

try:
    n = int(argv[1])
except TypeError:
    print("Must not be > 20")

if int(n) <= 20:
    pass
elif int(n) > 20:
    raise TypeError("Must not be > 20")
else:
    raise TypeError("Must be numeric")