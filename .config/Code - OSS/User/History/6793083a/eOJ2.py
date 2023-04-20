
n = 42
user_input = int(input("Enter a positive number: "))
if user_input < n:
    print(int(user_input - n))
elif user_input >= n:
    print(abs(int(user_input - n)))