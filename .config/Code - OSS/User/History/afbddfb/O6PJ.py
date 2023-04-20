

def find_in_list(i, lst):
    try:
        return lst[i]
    except IndexError:
        print("index out of range")



DAY = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(find_in_list(3, DAY))
print(find_in_list(8, DAY))

