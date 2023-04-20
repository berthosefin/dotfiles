

n = 42
user_input = -1
while user_input < 0:
    try:
        user_input = int(input("Enter a positive number: "))
    except:
        print("Number SVP!!!")

if user_input < n:
    print(int(n - user_input))
elif user_input >= n:
    print(abs(int(n - user_input)))