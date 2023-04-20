from seven_wonders import seven_wonders

def has_pyramid(lst: list):
    return bool([True if "Pyramid" else False in lst])


print(has_pyramid(seven_wonders()))
print(has_pyramid(["salad", "tomato", "onion"]))
print(has_pyramid(["Cube", "Pyramid", "Tower"]))