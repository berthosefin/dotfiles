from seven_wonders import seven_wonders

def has_pyramid(lst: list):
    for i in lst:
        if "Pyramid" in lst:
            return True
        else:
            return False
    return [True if "Pyramid" in lst else False for i in lst]


print(has_pyramid(seven_wonders()))
print(has_pyramid(["salad", "tomato", "onion"]))
print(has_pyramid(["Cube", "Pyramid", "Tower"]))