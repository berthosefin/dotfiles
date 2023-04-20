

def empty_rectangle(h, w):
    print("*" * w)
    for i in range(h-2):
        if h and w > 0:
            print("*" * w)
        else:
            print()
    print("*" * w)

full_rectangle(3, 5)