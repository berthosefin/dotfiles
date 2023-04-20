from seven_wonders import seven_wonders


def add_eighth_wonder(lst: list, wonder: str):
    nlst = lst.append(wonder)
    return nlst


add_eighth_wonder(seven_wonders(), "Death Start")