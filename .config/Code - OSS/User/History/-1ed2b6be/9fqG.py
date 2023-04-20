from seven_wonders import seven_wonders


def get_third_wonder(lst: list):
    [print(l) for l in lst]
    for l in lst:
        print(l[2])

get_third_wonder(seven_wonders())