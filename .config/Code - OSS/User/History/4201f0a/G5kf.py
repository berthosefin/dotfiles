

secret = input("Enter a secret: ")
star_nbr = len(secret[:-4])
print("*" * star_nbr + secret[-4:])