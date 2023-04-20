

def empty_rectangle(h, w):
    if h and w > 0:
        print("*" * w)
        for i in range(h-2):
            print("*" + str(" " * w-2) + "*")
        print("*" * w)
    else:
        print()

empty_rectangle(3, 5)