



def advanced_pattern(lst, h, w):
    for l in lst:
        if l == "full":
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
            pass


advanced_pattern(["full", "empty"], 3, 5)
print()
advanced_pattern(["empty"], 3, 5)
