

def find_in_list(i, lst):
    if i < len(lst):
        return lst[i]
    else:
        return "list index out of range"


def exceptions_light_filter(i, lst):
    pass


DAY = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(find_in_list(3, DAY))
print(find_in_list(8, DAY))

