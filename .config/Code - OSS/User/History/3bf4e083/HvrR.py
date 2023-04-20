

max = ""
while not max.isdigit():
    max = input("How many char max? (Number) ")

# user_input = ""
# len_user_input = len(user_input)
while True:
    user_input = input("It will repeat: ")
    len_user_input += len(user_input)
    if len_user_input < int(max):
        print(user_input)
    else:
        break