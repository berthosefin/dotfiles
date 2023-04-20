from seven_wonders import seven_wonders


def print_wonders_with_shift(lst: list):
    res = [" " * (len(lst) - 1) + l for l in lst]
    print(res)


print_wonders_with_shift(seven_wonders())