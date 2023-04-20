

max = 0
while not max.isdigit:
    max = int(input("How many char max? "))
user_input = ""
len_user_input = len(user_input)
while len_user_input < max:
    user_input = input("It will repeat: ")
    len_user_input += len(user_input)
