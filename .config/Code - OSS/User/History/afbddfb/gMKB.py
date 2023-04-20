

def find_in_list(i, lst):
    try:
        return lst[i]
    except IndexError:
        print("list index out of range")



DAY = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(find_in_list(3, DAY))

