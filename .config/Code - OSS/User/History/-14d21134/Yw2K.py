

def rectangle(h, w):
    if h > 0 and w > 0:
        for i in range(h):
            for j in range(w):
                print("*", end="")
            print()
            print()


def empty_rectangle(h, w):
    if h > 0 and w > 0:
        for i in range(h):
            for j in range(w):
                if i == 0 or i == h or j == 1 or j == w-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()


def diagonal_pattern(lst, h, w):
    for l in lst:
        if "diagonal" in words:
            di



def advanced_pattern(lst, h, w):



advanced_pattern(["empty", "full", "empty", "diagonal"], 3, 10)
print()
advanced_pattern(["empty", "potato", "diagonal"], 6, 6)
