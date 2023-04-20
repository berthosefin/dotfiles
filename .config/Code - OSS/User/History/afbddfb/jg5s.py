

def find_in_list(i, lst):
    return lst[i]


def exceptions_light_filter(i, lst):
    try:
        return find_in_list(i, lst)
    except IndexError:
        return



DAY = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# print(find_in_list(3, DAY))
# print(find_in_list(8, DAY))

print(exceptions_light_filter(3, DAY))
print(exceptions_light_filter(8, DAY))
print(exceptions_light_filter("nope", DAY))

