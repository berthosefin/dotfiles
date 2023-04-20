from seven_wonders import seven_wonders


def get_wonder_at_index(lst: list, i: int):
    return lst[i] if i <= len(lst)


print(get_wonder_at_index(seven_wonders(), 6))
print(get_wonder_at_index(seven_wonders(), 8))
print(get_wonder_at_index(["salad", "tomato", "onion"], 0))


