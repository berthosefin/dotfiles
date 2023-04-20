from seven_wonders import seven_wonders


def add_eighth_wonder(lst: list, wonder: str):
    nlst = [l and wonder for l in lst]
    return nlst


print(add_eighth_wonder(seven_wonders(), "Death Start"))