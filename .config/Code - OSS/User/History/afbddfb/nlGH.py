

def find_in_list(i, lst):
    return lst[i]


def exceptions_light_filter(i, lst):
    try:
        find_in_list(i, lst)
    except IndexError:
        return None



DAY = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(find_in_list(3, DAY))
# print(find_in_list(8, DAY))

