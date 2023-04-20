from seven_wonders import seven_wonders


def has_pyramid(lst: list):
    return [True if l == "Pyramid" else False in lst]


print(has_pyramid(["salad", "tomato", "onion"]))