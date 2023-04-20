from seven_wonders import seven_wonders


def add_eighth_wonder(lst: list, wonder: str):
    return [l for l in lst].append(wonder)


add_eighth_wonder(seven_wonders(), "Death Start")