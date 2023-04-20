

def advanced_pattern(lst, h, w):
    if h > 0 and w > 0:
        for l in lst:
            if l == "full":
                [print("*" * w) for i in range(h)]
            elif l == "empty":
                if h > 2:
                    print("*" * w)
                    for i in range(h-2):
                        if w < 2:
                            print("*")
                        else:
                            print("*" + " " * (w-2) + "*")
                    print("*" * w)
                else:
                    [print("*" * w) for i in range(h)]
            elif l == "diagonal":
                if h == w:
                    print("*" * w)
                    for i in range(h-2):
                        if w < 2:
                            print("*")
                        else:
                            print("*" + " " * (w-2) + "*")
                    print("*" * w)
    else:
        print()


advanced_pattern(["empty", "full", "empty", "diagonal"], 3, 10)
print()
advanced_pattern(["empty", "potato", "diagonal"], 6, 6)
