from seven_wonders import seven_wonders


def get_odd_wonders(lst: list):
    res = sorted([l for i, l in enumerate(lst) if i % 2 != 0])
    return res



print(get_odd_wonders(seven_wonders()))
print(get_odd_wonders(["salad", "tomato", "onion"]))