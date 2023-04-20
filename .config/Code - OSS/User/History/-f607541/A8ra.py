

def pattern(lst, h, w):
    if "full" in lst:
        [print("*" * w) if h > 0 and w > 0 else print() for i in range(h)]
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
    elif "diagonal" in lst:
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
        pass


pattern(["full"], 3, 5)
print()
pattern(["empty"], 3, 5)
