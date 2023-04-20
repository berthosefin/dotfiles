

# method find
mail = input("Give me your email: ")
index_start = mail.find("@")
index_end = mail.find(".")
print(mail[index_start+1:index_end])