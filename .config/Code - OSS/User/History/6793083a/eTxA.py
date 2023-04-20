

n = 42
while user_input < 0:
    user_input = int(input("Enter a positive number: "))
    if user_input < n:
        print(int(n - user_input))
    elif user_input >= n:
        print(abs(int(n - user_input)))