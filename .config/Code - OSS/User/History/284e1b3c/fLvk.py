from seven_wonders import seven_wonders


def print_wonders_with_shift(lst: list):
    [print(" " * i + l) for l in lst for i = (len(lst) - 1)]

    i = len(lst) - 1
    for l in lst:
        print(" " * i + l)
        i -= 1


print_wonders_with_shift(seven_wonders())