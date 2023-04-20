from seven_wonders import seven_wonders


def find_locations(lst: list):
    for l in lst:
        print(l)


print(find_locations(seven_wonders()))
print(find_locations(["Eiffel Tower of Paris", "Leaning Tower of Pisa", "Alhambra of Granada"]))