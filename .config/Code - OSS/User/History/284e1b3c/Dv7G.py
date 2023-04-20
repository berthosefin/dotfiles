from seven_wonders import seven_wonders


def print_wonders_with_shift(lst: list):
    i = len(lst)
    for l in lst:
        print(" " * i + l)
        i -= 1


print_wonders_with_shift(seven_wonders())