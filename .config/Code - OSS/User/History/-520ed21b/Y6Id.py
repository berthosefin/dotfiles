from seven_wonders import seven_wonders

def has_pyramid(lst: list):
    for i in lst:
        if "Pyramid" in lst:
            return True
        else:
            return False


print(has_pyramid(seven_wonders()))
print(has_pyramid(["salad", "tomato", "onion"]))
print(has_pyramid(["Cube", "Pyramid", "Tower"]))