

secret = input("Enter a secret: ")
star = len(secret[0:-4])
print("*" * star + secret[-4:])