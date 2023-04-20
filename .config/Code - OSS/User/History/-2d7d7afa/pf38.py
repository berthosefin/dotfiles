from seven_wonders import seven_wonders


def find_locations(lst: list):
    for l in lst:
        print(l.split(" ")[-1])


print(find_locations(seven_wonders()))
print(find_locations(["Eiffel Tower of Paris", "Leaning Tower of Pisa", "Alhambra of Granada"]))