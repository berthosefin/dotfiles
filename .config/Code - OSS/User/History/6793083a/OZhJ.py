

n = 42
user_input = -1
while user_input < 0:
    try:
        user_input = int(input("Enter a positive number: "))
    except:
        print("Number !!!")

if user_input < n:
    print(n - user_input)
elif user_input >= n:
    print(abs(n - user_input))