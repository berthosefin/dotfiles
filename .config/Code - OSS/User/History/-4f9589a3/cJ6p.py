from seven_wonders import seven_wonders

def exclude_wonders(lst: list):
    return lst[1:-1]


print(exclude_wonders(seven_wonders()))