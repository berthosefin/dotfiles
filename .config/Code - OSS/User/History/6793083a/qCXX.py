

n = 42
c = 0
while c == 0:
    user_input = int(input("Enter a positive number: "))

    if user_input < n:
        print(int(n - user_input))
        c += 1
    elif user_input >= n:
        print(abs(int(n - user_input)))
        c += 1