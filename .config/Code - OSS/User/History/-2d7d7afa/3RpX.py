from seven_wonders import seven_wonders


def find_locations(lst: list):
    return [l.split(" ")[-1] for l in lst]


print(find_locations(seven_wonders()))
print(find_locations(["Eiffel Tower of Paris", "Leaning Tower of Pisa", "Alhambra of Granada"]))