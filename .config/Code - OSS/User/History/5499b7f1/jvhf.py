from seven_wonders import seven_wonders


def get_odd_wonders(lst: list):
    return [l for l in lst if l]


print(get_odd_wonders(seven_wonders()))
print(get_odd_wonders(["salad", "tomato", "onion"]))