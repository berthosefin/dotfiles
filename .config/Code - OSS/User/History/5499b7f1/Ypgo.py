from seven_wonders import seven_wonders


def get_odd_wonders(lst: list):
    for l in lst:
        print(l)


print(get_odd_wonders(seven_wonders()))
print(get_odd_wonders(["salad", "tomato", "onion"]))