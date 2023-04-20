

def between_0_and_100(n):
    if n < 0:
        res = 0
    elif res > 100:
        res = 100
    else:
        res = n
    return res


print(between_0_and_100(-12))
print(between_0_and_100(0))
print(between_0_and_100(1))
print(between_0_and_100(42))
print(between_0_and_100(100))
print(between_0_and_100(2000))