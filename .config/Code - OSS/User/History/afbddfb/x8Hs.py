

def find_in_list(i, lst):
    return lst[i]


def exceptions_light_filter(i, lst):
    try:
        return find_in_list(i, lst)
    except (IndexError, TypeError):
        return

def exceptions_filter_everything(i, lst):
    try:
        return find_in_list(i, lst)
    except:
        return



DAY = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# print(find_in_list(3, DAY))
# print(find_in_list(8, DAY))

# print(exceptions_light_filter(3, DAY))
# print(exceptions_light_filter(8, DAY))
# print(exceptions_light_filter("nope", DAY))

print(exceptions_filter_everything(3, DAY))
print(exceptions_filter_everything(8, DAY))
print(exceptions_filter_everything("nope", DAY))

