

def betwenn_0_and_100(n: int):
    if n < 0:
        res = 0
    elif n > 100:
        res = 100
    else:
        res = n
    return res


print(betwenn_0_and_100(-12))
print(betwenn_0_and_100(0))
print(betwenn_0_and_100(1))
print(betwenn_0_and_100(42))
print(betwenn_0_and_100(100))
print(betwenn_0_and_100(2000))