

def pattern(lst, h, w):
    if lst == "full":
        if h > 0 and w > 0:
            for i in range(h):
                print("*" * w)
            else:
                print()
    elif lst == "empty":
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


pattern(["full", 3, 5])