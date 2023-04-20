from seven_wonders import seven_wonders


def print_wonders_with_shift(lst: list):
    [print(" " * (len(lst) - 1) + l) for l in lst]


print_wonders_with_shift(seven_wonders())