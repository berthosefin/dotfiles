from seven_wonders import seven_wonders


def print_wonders_with_shift(lst: list):
    for l in lst:
        print(" " * len(lst) + l)


print_wonders_with_shift(seven_wonders())