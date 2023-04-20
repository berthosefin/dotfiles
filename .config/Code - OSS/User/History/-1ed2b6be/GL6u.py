from seven_wonders import seven_wonders


def get_third_wonder(lst: list):
    return str([strl for l in lst if l == lst[2]])

print(get_third_wonder(seven_wonders()))
print(get_third_wonder(["salad", "tomato", "onion"]))