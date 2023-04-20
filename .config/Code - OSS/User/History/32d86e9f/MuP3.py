

# method find
mail = input("Give me your email: ")
index_arobase = mail.find("@")
mail_operator = mail[index_arobase+1:].split(".")[0]
print(mail_operator)

# method split
# mail = input("Give me your email: ")
# mail_split = mail.split("@")[1].split(".")[0]
# print(mail_split)