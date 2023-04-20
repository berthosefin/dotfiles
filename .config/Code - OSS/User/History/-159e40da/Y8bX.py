from seven_wonders import seven_wonders


def unvisited_wonders(wonders: list, lst: list):
    return sorted([l for l in wonders if not l in lst].sort())


print(unvisited_wonders(seven_wonders(), ["Hanging Gardens", "Temple of Artemis", "Mausoleum", "Colossus"]))
print(unvisited_wonders(["salad", "tomato", "onion"], ["onion"]))