from seven_wonders import seven_wonders


def has_all_wonders(lst: list):
    return True if lst == seven_wonders() else False


print(has_all_wonders(seven_wonders()))
print(has_all_wonders(["Test", "Tost"]))