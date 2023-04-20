from seven_wonders import seven_wonders


def print_wonders_with_shift(lst: list):
    [print(str(" " * i + l) for i in range(len(lst) - 1) for l in lst]

    i = len(lst) - 1
    for l in lst:
        print(" " * i + l)
        i -= 1


print_wonders_with_shift(seven_wonders())