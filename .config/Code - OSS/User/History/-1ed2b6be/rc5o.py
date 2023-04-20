from seven_wonders import seven_wonders


def get_third_wonder(lst: list):
    return [l for l in lst if l == lst[2]]

get_third_wonder(seven_wonders())
get_third_wonder(["salad", "tomato", "onion"])