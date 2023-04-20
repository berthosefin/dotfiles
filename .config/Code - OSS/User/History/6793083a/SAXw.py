

C = 42
user_input = -1
while user_input < 0:
    try:
        user_input = int(input("Enter a positive number: "))
    except:
        print("Number !!!")

if user_input < C:
    print(C - user_input)
elif user_input >= C:
    print((C - user_input)*2)