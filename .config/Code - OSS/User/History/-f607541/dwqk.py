

def pattern(lst, h, w):
    if "full" in lst:
        if h > 0 and w > 0:
            for i in range(h):
                print("*" * w)
            else:
                print()
    elif "empty" in lst:
        if h > 0 and w > 0:
            print("*" * w)
            for i in range(h-2):
                if w < 2:
                    print("*")
                else:
                    print("*" + " " * (w-2) + "*")
            print("*" * w)
        else:
            print()
    else:
        print("past")


pattern(["full"], 3, 5)