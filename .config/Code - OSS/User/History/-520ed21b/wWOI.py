

def has_pyramid(lst: list):
    return bool([True if "Pyramid" else False in lst])


print(has_pyramid(["salad", "tomato", "onion"]))
print(has_pyramid(["Cube", "Pyramid", "Tower"]))