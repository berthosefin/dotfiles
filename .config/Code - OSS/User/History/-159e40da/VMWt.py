from seven_wonders import seven_wonders


def unvisited_wonders(wonders: list, lst: list):
    return [l for l in wonders.sort() if not l in lst]


print(unvisited_wonders(seven_wonders(), ["Hanging Gardens", "Temple of Artemis", "Mausoleum", "Colossus"]))
print(unvisited_wonders(["salad", "tomato", "onion"], ["onion"]))