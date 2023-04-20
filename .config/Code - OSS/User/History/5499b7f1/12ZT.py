from seven_wonders import seven_wonders


def get_odd_wonders(lst: list):
    return [l for i, l in enumerate(lst) if i % 2 != 0]



print(get_odd_wonders(seven_wonders()))
print(get_odd_wonders(["salad", "tomato", "onion"]))