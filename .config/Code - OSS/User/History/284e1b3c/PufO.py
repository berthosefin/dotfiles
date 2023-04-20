from seven_wonders import seven_wonders


def print_wonders_with_shift(lst: list):
    print([" " * i + l for i, l in enumerate(lst)])

print_wonders_with_shift(seven_wonders())