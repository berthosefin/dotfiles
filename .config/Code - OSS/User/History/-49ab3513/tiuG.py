from seven_wonders import seven_wonders


def add_eighth_wonder(lst: list, wonder: str):
    return [l + wonder for l in lst]


print(add_eighth_wonder(seven_wonders(), "Death Start"))