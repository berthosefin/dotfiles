

def full_rectangle(h, w):
    if h and w > 0:
        for i in range(h):
            print("*" * w)
    else:
        print()

full_rectangle(3, 5)
full_rectangle(3, -5)