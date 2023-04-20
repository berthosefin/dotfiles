

max = ""
while not max.isdigit():
    max = input("How many char max? (Number)")
user_input = ""
len_user_input = len(user_input)
while len_user_input < max:
    user_input = input("It will repeat: ")
    len_user_input += len(user_input)
