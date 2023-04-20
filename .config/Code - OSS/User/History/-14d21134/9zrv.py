

def pattern(lst, h, w):
    if h > 0 and w > 0:
        if "full" in lst:
            [print("*" * w) for i in range(h)]
        elif "empty" in lst:
            print("*" * w)
            for i in range(h-2):
                if w < 2:
                    print("*")
                else:
                    print("*" + " " * (w-2) + "*")
            print("*" * w)
        elif "diagonal" in lst:
            if h == w:
                print("diagonal")
    else:
        print()


pattern(["full"], 3, 5)
print()
pattern(["empty"], 3, 5)
