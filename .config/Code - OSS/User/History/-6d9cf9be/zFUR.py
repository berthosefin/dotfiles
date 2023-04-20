

def est_premier(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
        else:
            return True


print(est_premier(22))