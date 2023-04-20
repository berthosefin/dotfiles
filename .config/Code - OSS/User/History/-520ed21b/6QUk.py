from seven_wonders import seven_wonders

def has_pyramid(lst: list):
    hp = [True if "Pyramid" in lst else False]
    res = bool(hp)
    return res


print(has_pyramid(seven_wonders()))
print(has_pyramid(["salad", "tomato", "onion"]))
print(has_pyramid(["Cube", "Pyramid", "Tower"]))