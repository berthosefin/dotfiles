from seven_wonders import seven_wonders

def has_pyramid(lst: list):
    return [True if "Pyramid" else False for l in lst]


print(has_pyramid(seven_wonders()))
print(has_pyramid(["salad", "tomato", "onion"]))
print(has_pyramid(["Cube", "Pyramid", "Tower"]))